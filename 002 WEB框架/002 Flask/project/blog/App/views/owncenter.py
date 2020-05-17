from flask import Blueprint,render_template,url_for,redirect,flash,request,current_app
from App.forms import UserInfo  # 导入个人信息显示user模型类
from flask_login import current_user,login_required
from App.models import Posts  # 导入博客的模型
from App.forms import SendPosts,Upload  # 导入发表博客模型类 用于编辑博客  # 导入文件上传表单类
from App.extensions import file,db
import os
from PIL import Image

owncenter = Blueprint('owncenter',__name__)


# 查看与修改个人信息
@owncenter.route('/user_info/',methods=['GET','POST'])
@login_required
def user_info():
    form = UserInfo()
    if form.validate_on_submit():
        current_user.age = form.age.data
        current_user.sex = int(form.sex.data)
        current_user.save()
    # 表单设置默认值
    form.username.data = current_user.username
    form.age.data = current_user.age
    form.sex.data = str(int(current_user.sex))
    form.email.data = current_user.email
    form.lastLogin.data = current_user.lastLogin
    form.register.data = current_user.registerTime
    return render_template('owncenter/user_info.html',form=form)


# 博客管理
@owncenter.route('/posts_manager/')
@login_required
def posts_manager():
    # 查看当前用户发表的所有博客  pid为0证明是博客内容而不是评论和回复的内容 state=0是所有人可见  按照时间降序查询
    posts = current_user.posts.filter_by(pid=0,state=0).order_by(Posts.timestamp.desc())
    return render_template('owncenter/posts_manager.html',posts=posts)


# 博客删除
# 任务：因为正常来说任何网站上的数据  用户执行删除处理 并不是真正的删除了 而是更改了状态 用户在执行玩删除 看不到数据 认为是真正的删除了 那其实是逻辑删除  并没有执行物理上的删除  所以咱们小伙伴希望更改为逻辑删除
# 实现：  在posts模型上 添加一个字段 当执行了删除 那么更改字段状态 那么用户就查看不到
@owncenter.route('/del_posts/<int:pid>/')
@login_required
def del_posts(pid):
    # 查询博客
    p = Posts.query.get(pid)
    # 判断该博客是否存在
    if p:
        # 执行删除
        flash('删除成功')
        p.delete() # 删除博客内容
        comment = Posts.query.filter(Posts.path.contains(str(pid))) # 删除评论和回复内容
        for posts in comment:
            posts.delete()
    else:
        flash('您要删除的博客不存在')
    return redirect(url_for('owncenter.posts_manager'))



# 博客编辑
@owncenter.route('/edit_posts/<int:pid>/',methods=['GET','POST'])
def edit_posts(pid):
    form = SendPosts()  # 实例化表单
    p = Posts.query.get(pid)  # 根据博客id 查询
    if not p:
        flash('该博客不存在')
        return redirect(url_for('owncenter.posts_manager'))
    if form.validate_on_submit():
        p.title = form.title.data  # 进行数据的存储
        p.article = form.article.data
        p.save()
        flash('博客更新成功')
        return redirect(url_for('owncenter.posts_manager'))
    form.title.data = p.title
    form.article.data = p.article
    return render_template('owncenter/edit_posts.html',form=form)


# 使用uuid扩展库生成唯一的名称
def random_filename(suffix):
    import uuid
    u = uuid.uuid4()
    return str(u)+'.'+suffix


# 图片缩放处理
def img_zoom(path,prefix='s_',width=100,height=100):
    # 打开文件
    img = Image.open(path)
    # 重新设计尺寸
    img.thumbnail((width, height))
    # 拆分传递进来的图片的路径 拆分进行前缀的拼接  /a/b.jpg  /a/s_b.jpg
    pathSplit = os.path.split(path)
    # 拼接好前缀 进行重新拼接成一个新的path
    path = os.path.join(pathSplit[0],prefix+pathSplit[1])
    # 保存缩放后的图片 保留原图片
    # 保存缩放
    img.save(path)

# 头像上传
@owncenter.route('/upload/',methods=['GET','POST'])
@login_required
def upload():
    form = Upload()
    if form.validate_on_submit():
        icon = request.files.get('icon')  # 获取上传对象
        suffix = icon.filename.split('.')[-1]  # 获取后缀
        newName = random_filename(suffix)  # 获取新的图片名称
        # 保存图片 以新名称
        file.save(icon,name=newName)
        delPath = current_app.config['UPLOADED_PHOTOS_DEST']
        # 删除之前上传过的图片
        if current_user.icon != 'default.png':  # 如果不等于 证明之前有上传过头像 否则就是没有上传过新头像
            os.remove(os.path.join(delPath,current_user.icon))
            os.remove(os.path.join(delPath,'b_'+current_user.icon))
            os.remove(os.path.join(delPath,'m_'+current_user.icon))
            os.remove(os.path.join(delPath,'s_'+current_user.icon))
        current_user.icon = newName  # 更改当前对象的图片名称
        db.session.add(current_user)  # 更新到数据库中
        db.session.commit()
        # 拼接图片路径
        path = os.path.join(delPath,newName)
        # 进行头像的多次缩放
        img_zoom(path)
        img_zoom(path,'m_',200,200)
        img_zoom(path,'b_',300,300)
    return render_template('owncenter/upload.html',form=form)


# 收藏管理
@owncenter.route('/my_favorite/')
@login_required
def my_favorite():
    # 查出当前用户的所有收藏的博客
    posts = current_user.favorites.all()
    return render_template('owncenter/my_favorite.html',posts=posts)


# 取消收藏
@owncenter.route('/del_favorites/<int:pid>/')
@login_required
def del_favorites(pid):
    # 判断是否收藏了
    if current_user.is_favorite(pid):
        # 调用取消收藏
        current_user.delete_favorite(pid)
    flash('取消收藏成功')
    return redirect(url_for('owncenter.my_favorite'))


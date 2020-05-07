from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

from  werkzeug.security import  generate_password_hash,check_password_hash

from app.ext import login_manager
from app.models import db, Channel, Article, User
from app.models import Tag
from app.forms import RegisterForm, LoginForm

bp = Blueprint('blue', __name__)

@bp.route('/create-db/')
def create_db():
    from app.models import db
    db.create_all()
    return 'db create'

@bp.route('/drop-db/')
def drop():
    from app.models import db
    db.drop_all()
    return 'db drop'

@bp.route('/',)
def index():
    return render_template('admin_dashboard.html')

@bp.route('/auth/login/',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email =form.email.data
        password = form.password.data
        next_url =request.args.get('next')
        user =User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            return redirect(next_url or url_for('blue.dashboard'))
        else:
            form.password.errors.append('用户名或密码错误')
            return render_template('login.html',form=form)
    return render_template('login.html',form=form)

@bp.route('/auth/register/',methods=['POST','GET'])
def register():
    form =RegisterForm()
    #检测request.method in[post,put,patch,delete]
    #将页面中的同名元素绑定到form中的同名属性
    #检验表单
    if form.validate_on_submit():
        print(form.data)
        #从通过验证后的表单form中获取数据
        nickname = form.nickname.data
        email = form.email.data
        password=form.password.data

        u= User()
        u.nickname =nickname
        u.email =email
        u.password=generate_password_hash(password)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('blue.login'))
    return render_template('register.html',form=form)

#flask-login 扩展默认情况下，会通过user id  来调用 load_user
@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(user_id)

@bp.route('/dashboard/')
def dashboard():
    return render_template('admin_dashboard.html')

@bp.route('/auth/logout/')
def logout():
    logout_user()
    return redirect(url_for('blue.login'))
#个人信息
@bp.route('/auth/profile/',methods =['POST','GET'])
@login_required
def profile():
    user =User.query.get(current_user.id)
    if request.method =='POST':
        nickname=request.form.get('nickname')
        email=request.form.get('email')
        user.nickname=nickname
        user.email =email
        if len('nickname')<1:
            message ='昵称不正确'
            return render_template('admin_profile.html',**locals())
        if len(email)<6:
            message = '邮箱不正确'
            return render_template('admin_profile.html', **locals())
        user.save()
        return redirect(url_for('blue.index'))

    return render_template('admin_profile.html',**locals())
#修改密码
@bp.route('/password/',methods =['POST','GET'])
@login_required
def password():
    user= User.query.get(current_user.id)
    user.save()
    if request.method =='POST':
        origin_password = request.form.get('origin_password')
        new_password = request.form.get('new_password')
        new_password_confirm=request.form.get('new_password_confirm')
        if new_password_confirm==new_password:
            if check_password_hash(user.password, origin_password):
                new_password=generate_password_hash(new_password)
                user.password =new_password
                user.save()
                message ='修改密码成功'
                return render_template('admin_dashboard.html',**locals())
            else:
                message ='原始密码不正确'
                return render_template('admin_password.html',**locals())
        else:
            message= '两次输入密码不一致'
            return render_template('admin_password.html', **locals())


    return render_template('admin_password.html')

#我的文章
@bp.route('/admin/article/article/')
@login_required
def admin_article():
    user = current_user
    page = int(request.args.get('page', 1))
    articles = Article.query.filter_by(user_id =user.id).paginate(page=page, per_page=2, error_out=False)
    return render_template('admin_article.html',articles=articles)
#文章添加
@bp.route('/admin/article/article/add/',methods =['POST','GET'])
def admin_article_add():
    channels = Channel.query.all()
    tags = Tag.query.all()
    if request.method == 'POST':
        title=request.form.get('title')
        txt_word=request.form.get('content')#文章正文内容
        channel_id =request.form.get('channel')
        channel_id=int(channel_id)

        user_id = current_user.id
        tag_list =request.form.getlist('tags')
        tag_list=[int(i) for i in tag_list]

        if len(title) <1 :
            error ='标题不能为空'
            return  render_template('admin_article_add.html',**locals())
        if channel_id ==0 :
            error ='请选择频道'
            return  render_template('admin_article_add.html',**locals())
        if len(tag_list) <1 :
            error ='请选择标签'
            return  render_template('admin_article_add.html',**locals())
        if len(txt_word) <4:
            error = '正文不能小于4个字符'
            return  render_template('admin_article_add.html',**locals())

        article = Article()
        article.title = title
        article.txt_word = txt_word
        article.user_id = user_id
        article.ch_id = channel_id
        _tags =Tag.query.filter(Tag.id.in_(tag_list))
        print(_tags)
        article.tags =_tags
        article.save()
        flash('文章保存成功')
        return redirect(url_for('blue.admin_article'))

    return  render_template('admin_article_add.html',**locals())

#文章修改
@bp.route('/admin/article/article/change/<int:id>/',methods = ['POST','GET'])
def admin_article_change(id):
    article=Article.query.get(id)
    channels =Channel.query.all()
    tags = Tag.query.all()
    if request.method =='POST':
        title=request.form.get('title')
        ch_id=int(request.form.get('channel'))
        txt_word=request.form.get('content')
        tag_list =request.form.getlist('tags')
        tag_list =[ int(i) for i in tag_list]
        article.title =title
        article.ch_id=ch_id
        article.txt_word=txt_word
        article.tags = Tag.query.filter(Tag.id.in_(tag_list)).all()
        if len(title)<1:
            error ='标题不能为空'
            return render_template('admin_article_change.html',**locals())
        if len(txt_word)<1:
            error ='正文不能为空'
            return render_template('admin_article_change.html',**locals())
        if len(tag_list)<1:
            error ='请选择标签'
            return render_template('admin_article_change.html',**locals())
        if ch_id == 0:
            error = '请选择频道'
            return render_template('admin_article_change.html', **locals())
        article.save()
        return redirect(url_for('blue.admin_article'))
    return  render_template('admin_article_change.html',**locals())

#文章删除
@bp.route('/admin/article/article/delete/<int:id>/')
def admin_article_delete(id):
    article = Article.query.get(id)
    article.delete()
    page = int(request.args.get('page', 1))
    articles = Article.query.paginate(page=page, per_page=2, error_out=False)
    return render_template('admin_article.html', articles=articles)
#频道
@bp.route('/admin/article/channel/')
@login_required
def admin_channel():
    page = int(request.args.get('page', 1))
    channels=  Channel.query.paginate(page=page,per_page =2,error_out =False)
    return  render_template('admin_channel.html',channels=channels)

#增加频道
@bp.route('/admin/article/channel/add/',methods=['GET','POST'])
def admin_channel_add():

    if request.method == 'POST':
        name = request.form.get('name')
        sort = request.form.get('sort')
        channel = Channel(ch_name=name,ch_sort=sort)
        channel.save()
        return redirect(url_for('blue.admin_channel'))
    return render_template('admin_channel_add.html ')
#频道修改
@bp.route('/admin/article/channel/change/<id>',methods=['POST','GET'])
def admin_channel_change(id):
    channel = Channel.query.get(id)
    if request.method == 'POST':
        ch_name=request.form.get('name')
        ch_sort=request.form.get('sort')
        channel.ch_name =ch_name
        channel.ch_sort=ch_sort
        channel.save()
    return render_template('admin_channel_change.html ',channel=channel)

#频道删除
@bp.route('/admin/article/channel/delete/<id>')
def admin_channel_delete(id):
    channel = Channel.query.get(id)
    channel.delete()
    page = int(request.args.get('page', 1))
    channels = Channel.query.paginate(page=page, per_page=2, error_out=False)
    return render_template('admin_channel.html',channels=channels)



#标签列表
@bp.route('/admin/article/tag/')
@login_required
def admin_tag():
    page =int(request.args.get('page',1))
    tags = Tag.query.paginate(page=page,per_page=2,error_out=False)
    return render_template('admin_tag_list.html',tags=tags)
#增加标签
@bp.route('/admin/article/tag/add/',methods=['GET','POST'])
def admin_tag_add():
    if request.method =='POST':
        name=request.form.get('name')
        tag=Tag()
        tag.tag_name = name
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for('blue.admin_tag'))
    return render_template('admin_tag_add.html')
#修改标签
@bp.route('/admin/article/tag/change/<int:id>/',methods=['POST','GET'])
def admin_tag_change(id):
    tag = Tag.query.get(id)
    if request.method == 'POST':
        name = request.form.get('name')
        tag.tag_name=name
        tag.save()
        return redirect(url_for('blue.admin_tag'))
    return render_template('admin_tag_change.html', tag=tag)
#删除标签
@bp.route('/admin/article/tag/delete/<int:id>/')
def admin_tag_delete(id):
    tag=Tag.query.get(id)
    db.session.delete(tag)
    db.session.commit()
    page = int(request.args.get('page', 1))
    tags = Tag.query.paginate(page=page, per_page=2, error_out=False)
    return render_template('admin_tag_list.html', tags=tags)














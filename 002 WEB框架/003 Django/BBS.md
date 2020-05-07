[TOC]

# BBS项目

## 需求分析

```python
'''
1. 注册：前后台校验、ajax注册、选取图形、图形上传
2、登录：ajax登录、图形验证码
3、博客首页
4、个人站点
5、文章的点赞与点踩
6、评论：根评论、子评论
7、后台管理
8、发布博客：防xss攻击
'''
```

## 数据库分析 (model )

![bbs表关系](.\img\bbs表关系.png)

```python
'''
用户表：User
	username：账号
	password：密码
	data_joined：注册时间
	email: 邮箱
	avatar：图像
	telephone：电话
	blog：博客站点(一对一)

博客站点表：Blog
	site: 站点域名
	name：站点名
	title：标题
	theme：站点主体样式
	category：拥有的分类(多对多)
	tag: 拥有的标签(多对多)
	
分类表：Category
	name：分类名
	
标签表：Tag
	name：标签名

文章表：Article
	title：文章标题
	desc：文章摘要
	content：文章内容
	create_time：发布事件
	blog：所属博客站点(一对多)
	category：所属分类(一对多)
	tag：拥有的标签(多对多)

点赞点踩表：UpOrDown  # user与article的点踩关系表
	user：点赞点踩用户(一对多)
	article：点赞点踩文章(一对多)
	is_up：点赞或点踩
	
评论表：Common  # user与article的评论关系表
	user：点赞点踩用户(一对多)
	article：点赞点踩文章(一对多)
	content：评论内容
	parent：父评论(自关联, 一对多)
'''
```

## 接口规则 ( url) 

```python
'''
演示：
http://api.map.baidu.com/place/v2/search?ak=6E823f587c95f0148c19993539b99295&output=json&query=%E8%82%AF%E5%BE%B7%E5%9F%BA&region=%E5%8C%97%E4%BA%AC

状态码：
SUCCESS("0000", "查询成功"),
NODATA("0001", "查询成功无记录"),
FEAILED("0002", "查询失败"),
ACCOUNT_ERROR("1000", "账户不存在或被禁用"),
API_NOT_EXISTS("1001", "请求的接口不存在"),
API_NOT_PER("1002", "没有该接口的访问权限"),
PARAMS_ERROR("1004", "参数为空或格式错误"),
SIGN_ERROR("1005", "数据签名错误")
UNKNOWN_IP("1099", "非法IP请求"),
SYSTEM_ERROR("9999", "系统异常");

规范制定：
{
    'statue': 0,
    'msg': 'ok',
    'data': {}
}
'''
```

## 相关配置 ( setting)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bbs',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456'
    }
}
AUTH_USER_MODEL = 'blog.User'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

import pymysql
pymysql.install_as_MySQLdb()
```

## 图形验证码

### 操作内存的流 - StringIO | BytesIO

```python
from io import StringIO, BytesIO
# 创建操作字符串的内存流
sf = StringIO()
# 往内存中写
sf.write('hello')
# 在内存总取
sf.getvalue()

# 创建操作二进制的内存流
bf = BytesIO()
# 往内存中写
bf.write('hello'.encode('utf-8'))
# 在内存总取
bf.getvalue()
```



### PIL：python图片操作库

```python
# 1、生成图片
from PIL import Image
# 生成一个Image类对象(准图片)：模式、尺寸、颜色
img = Image.new('RGB', (80, 80), color=(255, 0, 0))  # Type: Image
# 将Image类对象采用具体格式放入具体的文件流中
bf = BytesIO()  # eg: 内存字节流
img.save(bf, 'png')

# 2、产生文字颜色
from PIL import ImageFont
# 产生某种ttf格式的30px大小文字
img_font = ImageFont.truetype('*.ttf', 30)

# 3、画图
from PIL import ImageDraw
# 在具体的Image对象上画图
img_draw = ImageDraw.Draw(img)
# 画文字：xy轴、文本、颜色、ImageFont字体
img_draw.text((x, y), 'abc', 'red', img_font)
```



### 前端解析二进制流图片（了解）

```js
// 向指定url请求图片二进制流转换为blob:格式的src
var xhr = new XMLHttpRequest();
xhr.open('GET', url, true);  // url
xhr.responseType = "blob";
xhr.onreadystatechange = function () {
    if (xhr.readyState == 4) {
        if (xhr.status == 200) {
            var blod = this.response;
            var src = URL.createObjectURL(blod);  // src
        }
    }
};
xhr.send();
```



## Admin自动化数据管理界面

- admin的概念

```python
# Admin是Django自带的一个功能强大的自动化数据管理界面
# 被授权的用户可以直接在Admin中操作数据库
# Django提供了许多针对Admin的定制功能
```

- 配置并访问自动化数据管理界面

```python
# 终端项目目录创建一个超级用户：python3 manage.py createsuperuser
# eg：Username:root | Email:root@root.com | Password:1234qwer
# 浏览器Admin入口：http://127.0.0.1:8000/admin
# 设置Admin界面为中文环境：项目下settings.py，LANGUAGE_CODE = 'zh-Hans'
# 简体：zh-hans | 繁体：zh-hant | 美式英语：en-us
```

- 将指定映射添加到自动化数据管理界面

```python
# 应用下的admin.py中，注册映射对应关系的类
from . import models
admin.site.register(models.Article)
```

- 格式化界面字段显示名与表名

```python
# 为应用下models.py映射关系类重写__str__方法
class Article(models.Model):
    title = models.CharField(max_length=32, default='Title', verbose_name="标题")
    content = models.TextField(null=True, verbose_name="内容")
	# 重写__str__方法，格式化该类实例对象的表示方式
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
```

## 网络接口访问

**media**

```python
'''
1. 将用户上传的所有静态文件统一管理
	-- settings.py
		-- MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
2. 服务器会对外公开一下服务器静态资源
3. 对外公开的方式(配置url接口)，在接口中返回指定的静态资源(如何批量操作)
	-- from django.views.static import serve
	-- url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
'''
```

## 主页的布局

### 注册于站点进行绑定

```python
if user:
    # 创建该用户的站点
    u_name = user.username
    blog = Blog.objects.create(
        site=u_name,
        title=u_name + "的站点",
        theme=u_name + '.css',
        # 接口：后期添加个人中心界面，来修改或添加分类们与标签们
    )
    # 用户与站点进行绑定
    user.blog = blog
    user.save()
```


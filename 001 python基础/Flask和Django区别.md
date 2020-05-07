##### 一、框架区别

- Django的功能大而全，Flask只包含基本的配置。
  Django它是一站式解决思路，不用在选择应用的基础设施让花费大量时间。
- Flask是一个微框架，它只是一个内核，依赖于jinja2模板引擎和werkzeug WGI 工具集，其他很多功能都是以扩展的形式嵌入使用。
  - werkzeug WSGI 提供了路由处理，request和response封装，自带一个WSGIserver(开发测试用)
    Flask比Django更灵活，比如选择ORM,Flask在Django之后发布，吸取了Django的一些优点。-
  - Flask与非关系数据库的配合优于Django

##### 二、项目结构区别

- Django默认是把一个项目分为多个独立的应用，每个app有自己的model,view
- 而Flask认为一个项目是一个包含多个视图和模型的单个应用,Flask中有blueprints可以把组件分离

##### 三、模板区别

Flask模板引擎jinjia2和Django的模板引擎django基本一样

- 过滤器有点不同

  Django  {{ a. name | join:','   }}

  jinjia2 {{  a.name |join(',')  }}   #jinjia2的模板可能会传多个参数，用元组来封装

- jinjia2    for -else-endfor

  django  for-empty-endfor

##### 四、模型区别

- 定义

  Django: 

  ```
  from django.db import models
  class User(model.Model):
  	u_name =models.CharField(max_length=15)
  
  
  class Article(models.Model):
      a_name = models.CharField(max_length=15)
      user = models.ForeignKwy(to = User,on_delete=models.CACSDE)
      class Meta:
      	db_table = 'article'  # 如果未定义，数据库表名默认为 app名小写_模型名小写
      	
  #ForeignKey: 多对一
  #ManyToManyField:多对多
  #OneToOneField: 一对一
  ```

  Flask:  

  ```
  from flask_sqlalchemy import SQLAlchemy
  
  db = SQLAlchemy()
  
  class User(db.model):
  	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
  	U_name = db.COlumn(db.string(16),nullable = False)
  	articles = db.relationship('Article',backref='user',lazy='dynamic')
  	#relationship函数,sqlalchemy对关系之间提供的一种便利的调用方式，关联不同的表；
  	#第一个参数是关联模型的类名.backref参数是对关系提供反向引用的声明。
  	#relationship可以放在任何一个表中
  
  class Article(db.model):
  	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
  	a_name = db.COlumn(db.string(10),nullable = False)
  	user_id =db.Column(db.Integer,db.ForeignKey('user.id')) 
  	#db.ForeignKey() 用于定义外键，参数：另一方的表名.主键名
  	
  	tags = db.relationship('Tag', secondary='article_tags',		  backref=db.backref('articles', lazy='dynamic'),
                                 lazy='dynamic')
  	#多对多定义，relationship可以放在任何一个表中
  
  class Tag(db.model):
  	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
  	t_name = db.COlumn(db.string(20),nullable = False)	
  ```

- 查询所有数据的结果, all()方法:

  Django : querySet

  Flask :List

- 查询满足条件的数据结果，filter()方法

  Django: QUerySet

  Flask : BaseQuery objects  

  #另外Flask还有filter_by方法

- 添加记录

  Django:

  ```
  user= User()
  user.name =xxx
  user.save()
  ```

  Flask:

  ```
  user = User(xxx)
  db.session.add(user)
  db.session.commit()
  ```


##### 五、常用库整理

- flask-script

  为Flask提供强大的命令行操作，与Django shell类似

- flask-migrate

  用于数据库迁移

- flask-SQLAlchempy

  flask本身没有内置orm框架，需要依赖第三方。

  flask-sqlAlchemy是对SQLAchemy的进一步封装，当然也需要SQLchemy的支持

- flask-celery
  
-  Celery 是一个简单、灵活且可靠的，处理大量消息的分布式系统 ，我们通过用它来做异步任务，把一些耗时的操作异步进行。中间人常用的是rabbitmq和redis
  
- flask-login

  专门管理用户登录退出的扩展库，提供了login_user,logout_user,login_required,current_user等功能

- flask-wtf

  Flask与WTForms的集成，提供强大的Form安全和校验机制，与Django内置的Form功能类似

- flask-principal

  Flask强大的权限管理机制，灵活性强，提供了一个权限管理的基础框架

- flask-restful

  一个强大的flask restful框架，简单好用

- flask-api

  相当于Django REST Framework的Flask版本，是一个强大的Flask RESTful框架

- flask-httpauth

  Flask-HTTPAuth 提供了几种不同的 Auth 方法，比如 HTTPBasicAuth，HTTPTokenAuth，MultiAuth 和HTTPDigestAuth

- flask-Mail

  Flask-mail为Flask应用添加了SMTP邮件发送功能

- flask-user

  flask-user集成了用户管理相关功能，并允许对功能做定制性修改，其相关功能包括Register,

  confirm email,login,change password 

  flask-user 基于Flask-SQLAlchemy，NoSQL数据库无法使用

- Flask-security

  flask -security 让开发者能够很快的为应用添加常用的安全机制，其整合了Flask-login,Flask-mail,Flask-principal,Flask-script等应用，其安全机制包括：

  - Session based authentication

  - Role management

  - Password encryption

  - 等等好多

##### 六、flask-sqlalchemy

```
#手写sql语句
from sqlalchemy import create_engineengine = create_engine('mysql+pymysql://root:123456@182.92.7.134:3306/zhoujian')result = engine.execute('select *  from blog_tag')print(result.fetchall())
```

##### 七、flask-restful

```
from flask import Flask
from flask_restful import Api,Resource
app = Flask(__name__)
api = APi(app)

#双数
class PostList(Resource):
	def get(self):
		return '从数据库中查询 blog_posts 表中的人一组数据', 200
    def post(self):
        return '向 blog_posts 表中插入一条数据', 201

#单数
class PostDetail(Resource):
    
    def get(self, post_id):
        return '从 blog_posts 表中查询 id 为 {} 的记录'.format(post_id), 200

    def put(self, post_id):
        return '更新 blog_posts 表中 id 为 {} 的记录（请求时提供全部字段数据）'.format(post_id), 200
	# ...
       
        
api.add_resource(PostList,'/posts',endpoint='post_list')
api.add_resource(PostDetail,'/posts/<int:post_id>',endpoint='post_detail')

if __name == '__main__':
	app.run(debug=True)
```

八、flask-httpAuth

说明：RESTful API无法使用Flask-login扩展来实现用户认证(无法使用Cookie和session来保存用户信息)，需要使用Flask-HTTPAuth扩展

- 令牌(token)认证

  在对HTTP形式的API请求时，大部分情况我们是通过一个令牌，也就是Token来验证。

  - 使用HTTPTokenAuth对象，它也提供login_required装饰器来认证视图函数，error_handler装饰器来处理错误，它提供了verify_token装饰器来验证令牌。
  - 
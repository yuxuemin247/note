#### 1.钩子函数

```
flask常用请求钩子：

before_first_request：在处理app第一个请求前运行。

before_request：在每次请求前运行。

after_request：如果处理逻辑没有异常抛出，在每次请求后运行。

teardown_request：在每次请求后运行，即使处理发生了错误。

teardown_appcontext：在应用上下文从栈中弹出之前运行
```

```
定义钩子函数：相当于 django 中的 中间件

# before_request装饰的方法会加载到app的before_request_funcs列表中，按加载的顺序依次执行，不需要参数
@app.before_request
def test_before_request():
    print('before_request：2')

# before_first_request装饰的函数加载到before_first_request_funcs列表中，只不过在app第一次接收到请求后执行，其他时候不再执行
@app.before_first_request
def test_before_first_request():
    print('before_first_request：1')

# after_request装饰的函数加载到after_request_funcs列表中，传入的参数是response对象，可以对其进行拦截修改，必须返回一个response对象
@app.after_request
def test_after_request(response):
    print(response)
    print('after_request：3')
    return response
```

#### 2.四大内置对象

```

	request
		- 请求的所有信息
	session
		- 服务端会话技术的接口
	config
		当前项目的配置信息
		模板中可以直接使用
			config
		在python代码中
			current_app.config
			当前运行的app
			使用记得是在初始化完成之后
			用在函数中
	g
		global  全局在一次请求响应中生效，下一次就变成新的g了
		可以帮助开发者实现跨函数传递数据
```

#### 3、flask-login

flask-login是一个专门用来管理理用户登录退出的扩展库

- 安装

  ```
  pip install flask-login
  ```

- 添加扩展

  ```python
  from flask import Flask
  from flask.ext.login import LoginManager
  
  app = Flask(__name__)
  login_manager = LoginManager()
  login_manager.init_app(app)
  
  # 设置登录视图的名称，如果一个未登录用户请求一个只有登录用户才能访问的视图，则重定向到这里设置的登录视图。
  # 如果未设置登录视图，则直接返回401错误。
  login_manager.login_view = 'blue.login'
  
  # 设置登录错误信息
  login_manager.login_message = '请登录!'
  
  
  ```

- 编写用户类，继承自 UserMixin

  ```python
  from flask_login import UserMixin
  
  class User(UserMixin):
      pass
    
  #属性 is_authenticated     例如：{% if current_user.is_authenticated %}
  #当用户登录成功后，该属性为True。
  
  #属性 is_active
  #如果该用户账号已被激活，且该用户已登录成功，则此属性为True。
  
  #属性 is_anonymous
  #是否为匿名用户（未登录用户）。
  
  #方法 get_id()
  #每个用户都必须有一个唯一的标识符作为ID，该方法可以返回当前用户的ID，这里ID必须是Unicode。
  ```

- 实现回调

  ```
  @login_manager.user_loader
  def load_user(uid):
  	return User.query.get(uid)
  ```

  ```
   状态切换:
  login_user(user) # 登录   
  #登录成功以后，需要将登录状态保存到 session 中，比如：session['uid'] = user.id
  # 使用 flask-login 的 login_user() 就会帮我们完成上述工作
  
  
  
  logout_user # 退出登录
  
  状态查询:
      is_authenticated	# 登录状态
      is_anonymous	 # 匿名状态
      
  路由保护: @login_required 加在视图函数路由下
      login_required	# 保护需要登录才能访问的路路由
      
  当前用户:
      current_user  # 在哪里都可以使用，在模板中不不需要分配
  
  ```

  
## Day01

web 应用工作流程

#### web后端开发模式	

B/S	浏览器 - 服务器	browser / server

C/S 	客户端 - 服务器	client / server

在浏览器中输入一个网址，都发生了什么事情？

| 术语          | 解释                                                         |
| ------------- | ------------------------------------------------------------ |
| **URL/URI**   | 统一资源定位符/统一资源标识符，网络资源的唯一标识            |
| **域名**      | 与Web服务器地址对应的一个易于记忆的字符串名字                |
| **DNS**       | 域名解析服务，可以将域名转换成对应的IP地址                   |
| **IP地址**    | 网络上的主机的身份标识，通过IP地址可以区分不同的主机         |
| **HTTP**      | 超文本传输协议，构建在TCP之上的应用级协议，万维网数据通信的基础 |
| **反向代理**  | 代理客户端向服务器发出请求，然后将服务器返回的资源返回给客户端 |
| **Web服务器** | 接受HTTP请求，然后返回HTML文件、纯文本文件、图像等资源给请求者 |
| **Nginx**     | 高性能的Web服务器，也可以用作[反向代理](https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86)，[负载均衡] |
基于python的web （微） 框架

	重量级框架 django
		为了方便业务程序的开发，提供了丰富的工具及其组件
		
	轻量级框架 flask
		只提供web核心功能，自由灵活，高度定制
	
	Tornado 则与 Django 和 Flask 走不同的道路，Tornado 的主打功能是异步请求处理，适用于 IO 操作繁多的应用。
官方文档

	https://flask.palletsprojects.com/		英文
	http://docs.jinkan.org/docs/flask/     中文
flask依赖库

	flask依赖最重要的两个库：
	 Jinja2 模板引擎
	 Werkzeug  WSGI 工具集
	 
	还依赖：
		Click				命令行参数支持
		itsdangerous		数据加解密
		MarkupSafe			html/js 标签转义
		SQLALchemy
flask流行的主要原因

	 1 有非常齐全的官方文档，上手非常方便
	 2 有非常好的扩展机制和第三方扩展环境，工作中常见的软件都会有对应的扩展，动手实现扩展
	 也很容易
	 3 社区活跃度非常高，在github上flask的热度已经超过django
	 4 微型框架的形式给了开发者更大的选择空间

MVC

	一种软件设计架构规范
	Model
		数据的封装，数据的抽象，用来操作数据的入口
	View
		视图，主要用来呈现给用户的
	Controller
		控制器，主要用来接收用户请求（输入），并且协调模型和视图
		用来做视图和模型之间的数据的交互
	核心理念
		解耦
	实现结果
		将数据操作，页面展示，逻辑处理进行了拆分
MTV也叫做MVT

	Models                   M       M
		封装数据操作
		数据库的表和字段的定义
	Template 				 T		V
		模板
		用来展示数据
	Views					V		C
		视图函数
		相当于controller
		接收请求，协调模型和模板
```
HTTP

一个协议，应用层的、短连接协议

https://search.jd.com:443/Search?keyword=python

http://search.jd.com:80/Search?keyword=python

http/https: 协议
	http默认端口：80
	https默认端口：443
	小于 1024 的端口操作系统保留端口号
search.jd.com：域名
Search：请求路径
keyword=python：请求参数
```

```
WSGI，是一个规范

W，Web

S，server

G，gateway

I，interface
```



#### Flask基本使用

```
创建flask的虚拟环境
	python3 -m venv ~/.virtualenvs/flask_venv
	virtualenv -p /usr/local/bin/python3 ~/.virtualenvs/flask_venv
	
查看虚拟环境安装包
	pip freeze	# 查询除系统自带的安装包之外的第三方安装包
	pip list  # 查询所有安装包，包括系统自带的安装包和第三方包

虚拟环境迁移
	pip freeze > requirements.txt
		迁出
	pip install -r requirements.txt
		迁入
		
安装
	pip install flask
创建项目
  mkdir flask01  vim HelloFlask.py
  
	代码结构
		from flask import Flask
         app = Flask(__name__)

        @app.route("/")
        def index():
            return "Hello"
            
        app.run()
        
启动服务器  python  文件名字.py
	默认端口号  5000  只允许本机链接
	
run方法中添加参数
	在启动的时候可以添加参数  在 run() 中
	debug
		是否开启调试模式，开启后修改过python代码自动重启
	host
		主机，默认是127.0.0.1 指定为0.0.0.0代表本机ip
	port
		指定服务器端口号
	threaded
		是否开启多线程，最新版 flask 已经默认开启
```

```
flask 扩展库 flask-script
为 flask 提供命令行参数的支持
	安装
		pip install flask-script
		作用
			启动命令行参数
	初始化
		修改  文件.py为manager.py
		manager = Manager(app=app)
		修改 文件.run()为manager.run()
	运行
		python manager.py runserver -p xxx -h xxxx -d -r
	参数
    -p  端口 port
    -h  主机  host
    -d  调试模式  debug
    -r  重新加载  reload
```

```
简单体验
	index返回字符串
		@app.route('/index/')
        def index():
            return 'index'
	模板first.html
		@app.route('/html/')
        def hello():
            return render_template("first.html")
```

#### Flask基础结构

```
App
	templates
		模板
		默认也需要和项目保持一致
	static
		静态资源
		默认需要和我们的项目保持一致，在一个路径中，指的Flask对象创建的路径
	views
	models
	
manager.py
	第二个坑--封装__init__文件--
```

```
蓝图
	1. 宏伟蓝图（宏观规划）
	2. 蓝图也是一种规划，主要用来规划urls（路由）
	3. 蓝图基本使用
     - 初始化蓝图   bp = Blueprint('blue',__name__)
     - 调用蓝图进行路由注册  app.register_blueprint(blueprint=blue)
     - 蓝图必须和视图函数一起定义
```

```
Flask请求流程
	请求到路由 app.route()
	通过路由找到视图函数   
	视图函数和models交互
	模型返回数据到视图函数
	视图函数渲染模板
	模板返回给用户
```

```
带参数的请求
	从客户端或者浏览器发过来的请求带参数
	      @blue.route('/getstudents/<id>/')
          def getstudents(id):
              return '学生%s'+id
	路由中包含参数
		语法
			<converter:var_name>
				书写的converter可以省略，默认类型就是string
		converter
			string
				接收的时候也是str， 匹配到 / 的时候是匹配结束
				@blue.route('/getperson/<string:name>/')
                def getperson(name):
                    print(name)
                    print(type(name))
                    return name
			path
				接收的时候也是str， / 只会当作字符串中的一个字符处理
				@blue.route('/getperson1/<path:name>/')
                  def getperson1(name):
                      print(name)
                      print(type(name))
                      return name
			int
			     @blue.route('/makemoney/<int:money>/')
                  def makemoney(money):
                      print(type(money))
                      return '1'
			float
				@blue.route('/makemoneyfloat/<float:money>/')
                  def makemoney(money):
                      print(type(money))
                      return '1'
			uuid
				uuid 类型，一种格式
				@blue.route(('/getuu/'))
                  def getuu():
                      uu = uuid.uuid4()
                      print(uu)
                      return str(uu)

                  ------------------------------------
                  @blue.route('/getuuid/<uuid:uuid>/')
                  def getuuid(uuid):
                      print(uuid)
                      print(type(uuid))
                      return '2'
			any
				任意一个
				已提供选项的任意一个 而不能写any参数外的内容
				@blue.route('/getany/<any(a,b):p>/')
                def getany(p):
                    return '1'
```




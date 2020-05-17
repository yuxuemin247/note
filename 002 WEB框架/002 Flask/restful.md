#### 1.前后端分离

http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html

```
REST
整合网络和软件的一种架构模式
理解
	Representtational
		表现层
	State Transfer
		状态转换
	表现层状态转换
	
		资源（Resource）
	每一个URI代表一类资源
		对整个数据的操作
		增删改查
RESTful中更推荐使用HTTP的请求谓词（动词）来作为动作标识
	GET
	POST
	PUT
	DELETE
	PATCH
推荐使用json数据传输
```

```
状态码
	200 ok
	201 created
	202 Accepted
	204 删除成功 
	400 
	401
		没有认证
	403 
		没有权限
	404
	405 
	406 验证错误
	422 
	500
```

```
设计原则
	http（s）协议
	应该有自己专属域名
		在应用上添加一个api前缀
	都是名词，复数形式
	可以将版本号设计进去
		增量操作
	/collection/id/?id=xxx
```

#### 2.原生实现

```
概念：就是判断不同的请求方式，实现请求方法

MVC 没有模板--前后端分离
使用
	md5
	    eg：
	    def generate_password(password):
              hash = hashlib.md5()
              hash.update(password.encode("utf-8"))
              return hash.hexdigest()
	get
		坑---类型
		eg：
		@blue.route("/users/<int:id>/", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
        def users(id):
            if request.method == "GET":
                page = int(request.args.get("page", default=1))
                per_page = int(request.args.get("per_page", default=3))

                users = User.query.paginate(page=page, per_page=per_page, error_out=False).items
                users_dict = []
                for user in users:
                    users_dict.append(user.to_dict())

                data = {
                    "message": "ok",
                    "status": "200",
                    "data": users_dict
                }

                return jsonify(data)
	post
		eg:
            elif request.method == "POST":
                  # 更新或创建
                  username = request.form.get("username")
                  password = request.form.get("password")

                  data = {
                      "message": "ok",
                      "status": "422"
                  }

                  if not username or not password:
                      data["message"] = "参数不正确"
                      return jsonify(data), 422

                  user = User()
                  user.u_name = username
                  user.u_password = generate_password(password=password)

                  try:

                      db.session.add(user)
                      db.session.commit()
                      data["status"] = "201"
                  except Exception as e:
                      data["status"] = "901"
                      data["message"] = str(e)
                      return jsonify(data), 422

                  return jsonify(data), 201
	put
		eg:
			elif request.method == "PUT":
                      username = request.form.get("username")
                      password = request.form.get("password")
                      user = User.query.get(id)

                      user.u_name = username
                      user.u_password = generate_password(password)

                      db.session.add(user)
                      db.session.commit()

                      data = {
                          "message": "update success",
                      }

                      return jsonify(data), 201

	delete
		eg:
		    elif request.method == "DELETE":
                    user = User.query.get(id)

                    data = {
                        "message": "delete success"
                    }

                    if user:
                        db.session.delete(user)
                        db.session.commit()
                        return jsonify(data), 204
                    else:
                        data["message"] = "指定数据不存在"
                        return jsonify(data)

	patch
			eg:
			   elif request.method == "PATCH":
                        password = request.form.get("password")
                        user = User.query.get(id)
                        user.u_password = generate_password(password)

                        data = {
                            "messgage": "update success"
                        }

                        db.session.add(user)
                        db.session.commit()

                        return jsonify(data), 201
```

#### 3.flask-restful

```
框架简化开发
```

##### 使用

```
使用
	安装 pip install flask-restful
	初始化 
		urls---在init中调用init_urls
			api = Api()
			api.add_resource(Hello, "/hello/")
				Hello是一个类的名字  hello是路由
			def init_urls(app):
    		api.init_app(app=app)
    
	apis--基本用法
		继承自Resource
			class Hello(Resource):
		实现请求方法对应函数
			def get(self):
        		return {"msg": "ok"}

            def post(self):
                return {"msg": "create success"}
```

##### 定制输入输出

```
定制输入输出
	输出
		fields中的类型约束
			String
			Integer
			Nested
			List
				Nested
		@marshal_with的基本使用
			类型括号中还允许添加约束
				attribute
					指定连接对应名字
						attribute=名字
				default
					设置默认值
						default=404
		marshal_with特性
			        - 默认返回的数据如果在预定义结构中不存在，数据会被自动过滤
        	         - 如果返回的数据在预定义的结构中存在，数据会正常返回
                      - 如果返回的数据比预定义结构中的字段少，预定义的字段会呈现一个默认值
			        如果类型是Integer  那么默认值是  0
                     如果类型是String  那么默认值是null
                @marshal_with返回一个类对象
                @marshal_with返回一个列表
	输入
		使用了parser=reqparse.RequestParser()
		parser.add_argument("c_name", type=str)
        parser.add_argument("id", type=int, required=True, help="id 是必须的")
		parse = parser.parse_args()
		cat_name = parse.get("c_name")
        id = parse.get("id")
         print(id)
		在对象中添加字段
			对字段添加约束
			default
			required
				必须的参数
			help
				id是必须的
			action
				action=append
					c_name=tom&c_name=zs
		继承
			copy
			可以对已有字段进行删除和更新
			继承解析
    - 在整个项目中，通用字段可以创建一个基parser
    - 复用已有的部分参数转换数据结构
			parse_c parser.copy()   parse_c.remove_argument('')
```


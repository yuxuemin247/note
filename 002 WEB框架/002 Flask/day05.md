## Day05

#### 1.数据迁移

```
安装：
pip install flask-migrate


使用：
from flask import Flask
from flask_sqlalchemy import SQLalchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
db = SQLalchemy(app) #实例例化ORM

migrate = Migrate()
migrate.init_app(app,db)  #实例化迁移对象

manager = Manger(app)
manager.add_command('db',MigrateCommand) #添加迁移命令 别名为db



迁移步骤(命令)
(1) 迁移初始化(创建迁移⽬目录)
python manage.py db init

(2) 创建迁移文件
python manage.py db migrate

(3) 执⾏迁移
python manage.py db upgrade
```

#### 2. 分页

```
pagination
	分页器
	需要想要的页码
	每一页显示多少数据
	原生
	persons = Person.query.offset((page_num - 1) * per_page).limit(per_page)
	select * from users offset 0 limit 20
	select * from users offset 20 limit 40
	
	参数（page，page_per,False(是否抛异常）
	persons = Person.query.paginate(page_num, per_page, False).items


方法:paginate，分⻚页查询

参数:
	page:当前的⻚页码
	per_page:每⻚页的条数
	error_out:当查询出错时是否报错
	
返回值: 
	Pagination:分⻚页对象，包含了了所有的分⻚页信息
	
Pagination: 
	属性:
		page:当前⻚页码 
		per_page:每⻚页的条数，默认为20条 
		pages:总⻚页数
		total:总条数 
		prev_num:上⼀⻚页的⻚页码 
		next_num:下⼀⻚页的⻚页码 
		has_prev:是否有上一⻚页 
		has_next:是否有下一⻚页 
		items:当前⻚页的数据
		
	方法: 
	iter_pages:返回⼀一个迭代器器，在分⻚页导航条上显示的⻚码列表，显示不不完的时返回None
	prev:上⼀页的分页对象
	next:下一⻚的分页对象
```

```python
{# 分页显示的宏 #}
{% macro pagination_widget(pagination, endpoint) %}
    <ul class="pagination">
        <li{% if not pagination.has_prev %} class="disabled"{% endif %}>
            <a href="{% if pagination.has_prev %}{{ url_for(endpoint,page = pagination.page - 1, **kwargs) }}
            {% else %}#{% endif %}">&laquo;
            </a>
        </li>
        {% for p in pagination.iter_pages() %}
            {% if p %}
                {% if p == pagination.page %}
                    <li class="active">
                        <a href="{{ url_for(endpoint, page = p, **kwargs) }}">{{ p }}</a>
                    </li>
                {% else %}
                <li>
                    <a href="{{ url_for(endpoint, page = p, **kwargs) }}">{{ p }}</a>
                </li>
                {% endif %}
            {% else %}
            <li class="disabled">
                <a href="#">&hellip;</a>
            </li>
            {% endif %}
        {% endfor %}
        <li{% if not pagination.has_next %} class="disabled"{% endif %}>
            <a href="{% if pagination.has_next %}{{ url_for(endpoint,page = pagination.page + 1, **kwargs) }}{% else %}#{% endif %}">&raquo;</a>
        </li>
    </ul>
{% endmacro %}
```

####3.钩子函数

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
def test_after_request(resp):
    print(resp)
    print('after_request：3')
    return resp
```

#### 4.四大内置对象

```
四大内置对象
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
		global  全局
		可以帮助开发者实现跨函数传递数据
```


# Model模型

## 一、前期准备

#### (1) 在MySQL中创建数据库

create database 数据库名称 character set utf8;

#### (2) 安装pymysql

pip install pymysql

#### (3) 安装flask-sqlalchemy

pip install flask-sqlalchemy

#### (4) 导入与配置

```python
# 导入ORM模型
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
# 配置数据库连接
# 配置MySQL数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/lucky'
# 配置sqlite数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(os.getcwd(),'lucky.sqlite')
# 是否追踪数据的改变 发出警告  关闭
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 实例化ORM模型
db = SQLAlchemy(app)
manager = Manager(app)
```

## 三、设计模型

#### (1) 常见字段类型

| 类型名称     | python类型        | 说明                    |
| ------------ | ----------------- | ----------------------- |
| Integer      | int               | 存储整形                |
| SmallInteger | int               | 小整形                  |
| BigInteger   | int               | 长整形                  |
| Float        | float             | 浮点数                  |
| String       | str               | 字符串（不定长varchar） |
| Text         | str               | 大型文本                |
| Bollean      | bool              | 布尔类型                |
| Date         | datetime.date     | 日期                    |
| Time         | datetime.time     | 时间                    |
| DateTime     | datetime.datetime | 日期和时间              |

#### (2) 可选约束条件

| 选项        | 说明                        |
| ----------- | --------------------------- |
| primary_key | 是否设置为主键  默认False   |
| unique      | 是否设置唯一索引 默认Fale   |
| index       | 是否设置常规索引  默认False |
| nullable    | 是否可以为空 默认True       |
| default     | 设置默认值                  |

**注意：**

1. flask-sqlalchemy要求每个模型都要有一个主键 否则报错
2. 默认可以为空 设置默认值的时候 并不是更改表的结构设置默认值  而是在你没有给当前属性值的时候 会把默认值作为值进行传入



## 四、创建模型

**(1) 创建user模型类**

**实例：**

```python
# 创建user模型类
class User(db.Model):
    __tablename__ = 'user' # 起表名 默认不起为类名
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),default='lucky',index=True)
    age = db.Column(db.Integer,default=18)
    sex = db.Column(db.Boolean,default=True)
    info = db.Column(db.String(50),default='个人简介')
    def __str__(self):
        return 'username:'+self.username
```

**(2) 创建表**

**实例：**

```python
# 创建表
@app.route('/create/')
def create():
    db.create_all()
    return '创建表'
```

**(3) 删除表**

**实例：**

```python
# 删除表
@app.route('/drop/')
def drop():
    db.drop_all()
    return '删除'
```



## 五、数据的增删改查

#### (1) add 添加一条数据

**实例：**

添加数据方式一

```python
# 添加一条数据
@app.route('/insert_one/')
def insert_one():
    try:
        data = User()
        data.username = 'lucky'
        data.age = 18
        data.sex = False
        data.info = '我是帅气的lucky老师'
        db.session.add(data)
        # 事物提交
        db.session.commit()
    except:
        # 事物回滚
        db.session.reoooback()
    return '添加一条数据'
```

添加数据方式二

```python
# 添加一条数据
@app.route('/insert_one/')
def insert_one():
    try:
        u = User(username='lucky_boy')
        db.session.add(u)
        db.session.commit()
    except:
        db.session.rollback()
    return '添加一条数据'
```

**注意：**

1. sqlalchemy默认开启了事物处理
2. 每次对数据进行处理需要提交或者回滚 
   + db.session.commit()
   + db.session.rollback()

#### (2) add_all 添加多条数据

**实例：**

```python
# 添加多条数据
@app.route('/insert_many/')
def insert_many():
    try:
        u1 = User(username='张三',age=20)
        u2 = User(username='李四',age=22,sex=False)
        db.session.add_all([u1,u2])
        db.session.commit()
    except:
        db.session.rollback()
    return '添加多条数据'
```

#### (3) get 数据查询

**实例：**

```python
# 查询数据
@app.route('/select/')
def select():
    u = User.query.get(2)
    print(u)
    print(u.username)
    print(u.age)
    print(u.sex)
    return '查询'
```

#### (4) 数据的修改

**实例：**

```python
# 修改数据
@app.route('/update/')
def update():
    try:
        u = User.query.get(1)
        u.age = 19
        u.sex = True
        db.session.add(u)
        db.session.commit()
    except:
        db.session.rollback()
    return '修改'
```

#### (5) delete 数据的删除

**实例：**

```python
# 数据删除
@app.route('/delete/')
def delete():
    u = User.query.get(3)
    db.session.delete(u)
    db.session.commit()
    return '删除'
```



## 六、自定义封装模型类增删改的基类

#### (1) 模型类

**实例：**

```python
# 自定义封装模型基类
class DB_Base:
    # 添加一条数据
    def save(self):
        try:
            # self 代表当前当前实例化的对象
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    # 添加多条数据
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    # 删除
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
```

**类中继承**

```python
# 创建user模型类
class User(db.Model,DB_Base):
```
#### 使用自定义方法操作

#### (1) 添加一条数据

```python
# 添加一条数据
@app.route('/insert_one/')
def insert_one():
    # 使用自定义的基类进行添加操作
    u = User(username='孙悟空',age=200)
    u.save()
    return '添加一条数据'
```

#### (2) 添加多条数据

```python
# 添加多条数据
@app.route('/insert_many/')
def insert_many():
    u1 = User(username='八戒', age=300)
    u2 = User(username='沙僧', age=400, sex=False)
    User.save_all(u1,u2)
    return '添加多条数据'
```
#### (3) 修改数据

```python
# 修改数据
@app.route('/update/')
def update():
    u = User.query.get(6)
    u.sex = False
    u.save()
    return '修改'
```
#### (4) 删除数据

```python
# 数据删除
@app.route('/delete/')
def delete():
    u = User.query.get(7)
    u.delete()
    return '删除'
```



## 七、数据库操作

**查询集：**

查询数据的集合

**分类**

1. 原始查询集

   使用类名.query 得到的就是原始查询集 

2. 数据查询集

   通过过滤器方法  过滤原始查询集或者起亚数据查询集得到的查询集

**特点：**

链式调用

**模板show.html代码**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        table{
            border-collapse: collapse;
            margin: auto;
        }
        td{
            width:200px;
            height: 50px;
            line-height: 50px;
            text-align: center;
            border-bottom: 1px dotted red;
        }
    </style>
</head>
<body>
<table>
    <caption><h1>数据常规操作</h1></caption>
    <tr>
        <td>Id</td>
        <td>username</td>
        <td>age</td>
        <td>sex</td>
        <td>info</td>
    </tr>
    {% for row in data %}
        <tr>
            <td>{{ row.id }}</td>
            <td>{{ row.username }}</td>
            <td>{{ row.age }}</td>
            <td>{{ row.sex }}</td>
            <td>{{ row.info }}</td>
        </tr>
    {% endfor %}

</table>
</body>
</html>
```



#### (1) all() 查询所有

以列表形式返回

**实例：**

```python
@app.route('/test/')
def test():
    # all 查询所有
    u = User.query.all()
    print(u)
    return render_template('show.html',data=u)
```
#### (2) filter() 过滤 默认查询所有

类名.query.filter(【类名.属性名.运算符 值】)

```python
# filter 过滤
# 查询所有
u = User.query.filter()
# 查询性别为True的数据
u = User.query.filter(User.sex==True)
```

#### (3) filter_by() 只支持但条件查询

**格式：**

filter_by(属性名=值,【属性名=值】)

```python
# filter_by
# 查询username为lucky的数据
u = User.query.filter_by(username='lucky')
# 查询username为lucky的数据 并且性别为False
u = User.query.filter_by(username='lucky',sex=False)
```

#### (4) offset(num) 偏移数量

**格式：**

offset(5)

```python
# offset 偏移量
u = User.query.offset(2)
```

#### (5) limit(num) 取出num条数据

```python
# limit 取出num条数据
u = User.query.limit(3)
```

#### (6) offset 和 limit组合使用

```python
# limit 和 ofsset组合
u = User.query.offset(2).limit(2)
```

#### (7) order_by() 排序

**格式：**

order_by(类名.属性名)

**说明：**

1. 默认按照指定字段升序
2. -熟悉名 降序

```python
# order_by() 排序
# 按照年龄的升序
u = User.query.order_by(User.age)
# 按照年龄的降序
u = User.query.order_by(-User.age)
# 取出一条年龄最大的数据
u = User.query.order_by(-User.age).limit(1)
# 取出一条年龄第二大的数据
u = User.query.order_by(-User.age).offset(1).limit(1)
```

#### (8) first() 在查询集中取出第一条数据

```python
# first() 获取第一条数据
u = User.query.first()
```

#### (9) get(id的值) 根据id进行数据查询  如果查询不到返回None

```python
u = User.query.get(2)
```

#### (10) contains() 包含关系

```python
# contains() 包含
# 查询用户名中包含l的数据
u = User.query.filter(User.username.contains('l'))
```

#### (11) like 模糊查询

```python
# like 模糊查询
# 包含l
u = User.query.filter(User.username.like('%l%'))
# l作为开头
u = User.query.filter(User.username.like('l%'))
# l作为结尾
u = User.query.filter(User.username.like('%y'))
```

#### (12) startswith   endswith 以...开头  以...结尾

```python
# startswith endswith 以...开头结尾
u = User.query.filter(User.username.startswith('孙'))
u = User.query.filter(User.username.endswith('y'))
```

#### (13) 比较运算符

1. `__gt__`大于
2. `__lt__`小于
3. `__ge__`大于等于
4. `__le__`小于等于
5. `>`
6. `<`
7. `>=`
8. `<=`
9. `!=`
10. ==

**实例**

```python
# 比较运算符
# 查询id大于2的数据
u = User.query.filter(User.id.__gt__(2))
u = User.query.filter(User.id>2)
# 查询id小于等于2的数据
u = User.query.filter(User.id.__le__(2))
u = User.query.filter(User.id<=2)
```

#### (14) in_ 和 notin_ 是否包含在...范围内

```python
# 在...范围内
# 查询id为1,4的数据
u = User.query.filter(User.id.in_([1,4]))
# 查询id不为1,4的数据
u = User.query.filter(User.id.notin_([1,4]))
u = User.query.filter(~User.id.in_([1,4]))
```

#### (15) is null isnot 查询为空和不为null的数据

```python
# 查询为null的数据
u = User.query.filter(User.username.is_(None))
u = User.query.filter(User.username == None)
# 查询不为null的数据
u = User.query.filter(User.username.isnot(None))
u = User.query.filter(User.username!=None)
u = User.query.filter(~User.username.is_(None))
```

#### (16) 逻辑与

**导入**

from sqlalchemy import and_

**实例：**

```python
from sqlalchemy import and_
    # 逻辑于 and_
    # 查询性别为True 并且年龄大于20的数据
    u = User.query.filter(User.sex==True,User.age>20)
    u = User.query.filter(User.sex==True).filter(User.age>20)
    u = User.query.filter(and_(User.sex==True,User.age>20))
```

#### (17) 逻辑或

**导入：**

from sqlalchemy import or_

**实例：**

```python
# 逻辑或 or_
    # 查询性别为True 或者 年龄大于20的数据
    u = User.query.filter(or_(User.sex==True,User.age>20))
```

#### (18) 逻辑非

**导入：**

from sqlalchemy import not_

**实例：**

```python
# 逻辑非 not_
# 查询性别为False的数据
u = User.query.filter(not_(User.sex==True))
u = User.query.filter(~(User.sex==True))
```

**注意：**

逻辑非里面只能有一个条件

#### (19) count 统计函数

```python
# count 统计
# 统计性别为False的数据条数
u = User.query.filter(not_(User.sex==True)).count()
```

#### (20) concat() 连接

```python
# concat 连接
u = User.query.order_by(User.id.concat(User.age))
```



## 八、文件迁移 flask-migrate

#### (1) 安装

pip install flask-script

pip install flask-migrate

#### (2) 创建迁移对象

**实例：**

```python
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/lucky'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# 创建迁移对象
migrate = Migrate(app,db)
manager = Manager(app)
# 添加迁移命令
manager.add_command('db',MigrateCommand)
```

#### (3) 创建迁移目录

**命令：**

python manage.py db init

那么就会在工程目录下生成一个名为migrations的目录

#### (4) 生成迁移文件

python manage.py db migrate

就会在versions目录下生成一个迁移的文件

#### (5) 执行迁移(更新数据库)

python manage.py db upgrade

## 九、分页

```
pagination 
	原生
	persons = Person.query.offset((page_num -1)* per_page).limit(per_page)
	分页器
	参数(page,page_per,False(是否抛异常))
	per_pagination = Person.query.paginate(page_num,per_page,False)
	返回值：
		Pagination:分页对象，包含了所有的分页信息
	Pagination:
        属性：
            page:当前页码
            per_page:每页的条数，默认为20条
            pages:总页页数
            total:总条数
            prev_num:上一页的页码
            next_num:下一页的页码
            has_prev:是否有上一页
            has_next:是否有下一页
        方法：
        	iter_pages:返回一个迭代器，在分页导航条上显示页码列表，显示不完时返回None
        	prev:上一页的分页对象
        	next:下一页的分页对象	
```

```
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

## 十、模型关系

（1） 一对多

```
一对多
class Parent(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(30),unique=True)
    children=db.relationship("Child",backref="parent",lazy=True)


class Child(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
    
    #db.ForeignKey() 用于定义外键，参数：另一方的表名.主键名

relationship函数
	      sqlalchemy对关系之间提供的一种便利的调用方式，关联不同的表；
	      第一个参数是关联模型的类名
backref参数
          对关系提供反向引用的声明，在Child类上声明新属性的简单方法，之后可以在child.parent来获取这个地址的Parent；
lazy参数
          'select'/True（默认值）
              SQLAlchemy 会在使用一个标准 select 语句时一次性加载数据；
              会发送两条 SQL 语句，一条查 one 的一方，一条查 many 的一方
          'joined'/False
              让 SQLAlchemy 当父级使用 JOIN 语句是，在相同的查询中加载关系；
              会发送一条 SQL 语句，通过 LEFT JOIN 的方式 查询 one 一方和 many 一方的数据
          'subquery'
              类似 'joined' ，但是 SQLAlchemy 会使用子查询；
          'dynamic'：
              SQLAlchemy 会返回一个查询对象，在加载这些条目时才进行加载数据，大批量数据查询处理时推荐使用。会发送一条 SQL 语句，只查询 one 一方的数据，
                        many 一方的关联属性是一个 Query 对象，不会真正执行查询，
                       在需要时，调用 children.all() 真正去数据库中查询数据
              
ForeignKey参数
	      代表一种关联字段，将两张表进行关联的方式，表示一个parent的外键，设定上必须要能在父表中找到对应的id值
	      
添加
	eg：@blue.route('/add/')
        def add():
            p = Parent()
            p.name = '张三'
            c = Child()
            c.name = '张四'
            c1 = Child()
            c1.name = '王五'
            p.children = [c,c1]

            db.session.add(p)
            db.session.commit()

            return 'add success'
查
      eg:
      主查从 --》 Parent--》Child
      @blue.route('/getChild/')
      def getChild():
          clist = Child.query.filter(Parent.id == 1)
          for c in clist:
              print(c.name)
          return 'welcome to red remonce'
      从查主
      @blue.route('/getParent/')
      def getParent():
          p = Parent.query.filter(Child.id == 2)
          print(type(p))
          print(p[0].name)
   	  return '开洗'
```

（2）一对一

```
一对一
   一对一需要设置relationship中的uselist=Flase，不能设置 lazy，其他数据库操作一样。
```

（3）多对多

```
多对多
class Group(db.Model):
    __tablename__ = 'groups'
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(32), unique=True, nullable=False)

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(16), nullable=False)
    groups = db.relationship('Group', secondary='student_groups',
    								backref=db.backref('students', lazy='dynamic'),
          							lazy='dynamic')
    # 多对多关系定义，本质是双向的一对多关系
    # secondary 指定多对多关系中的关系表
# db.Table()
# 第一个参数：表名
# 其他参数：字段定义   
student_groups = db.Table('student_groups',
      	db.Column('id', db.Integer, primary_key=True),
   		db.Column('student_id', db.Integer,db.ForeignKey('students.id')),                         db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
                          )    
eg:视图函数中使用
@bp.route('/m2m-init/')
def m2m_init():
    g1 = Group(name='python')
    g2 = Group(name='html')
    g3 = Group(name='golang')

    db.session.add_all([g1, g2, g3])
    db.session.commit()
    
    return 'm2m_init'


@bp.route('/m2m-create/')
def m2m_create():
    python = Group.query.filter_by(name='python').first()
    html = Group.query.filter_by(name='html').first()
    golang = Group.query.filter_by(name='golang').first()

    tom_0 = Student.query.get(1)
    tom_1 = Student.query.get(2)

    python.students.append(tom_0)
    
    tom_1.groups.append(html)
   
   db.session.commit()
    
    return 'm2m_create'


@bp.route('/m2m-delete/')
def m2m_delete():
    python = Group.query.filter_by(name='python').first()
    html = Group.query.filter_by(name='html').first()

    tom_0 = Student.query.get(1)
    tom_1 = Student.query.get(2)

    # 删除一个不属于 student 对象的 group 会报错
    # tom_0.groups.remove(python)

    # 清空 html 组内的所有学生
    html.students = []

    db.session.commit()

    return 'm2m_delete'   
```

```
购物车添加
    @blue.route('/getcollection/')
	def getcollection():
          u_id = int(request.args.get('u_id'))
          m_id = int(request.args.get('m_id'))
          c = Collection.query.filter(Collection.u_id == u_id).filter_by(m_id = m_id)

          if c.count() > 0:
              print(c.first().u_id,c.first().m_id)
              # print(c)
              # print(type(c))
              # print('i am if')
              return '已经添加到了购物车中'
          else:
              c1 = Collection()
              c1.u_id = u_id
              c1.m_id = m_id
              db.session.add(c1)
              db.session.commit()
              return 'ok'
```

## 十一、Sqlalchemy优化

```
@app.after_request
def af_request(response):
    for query in get_debug_queries():
        if query.duration >= 2:
            current_app.logger.warning(
                    'Slow query: %s\nParameters: %s\nDuration: %fs\nContext:
                    %s\n' %(query.statement, query.parameters, query.duration,
                        query.context)
                    )
            return response
```

这个功能使用after_app_requestq请求钩子实现的，在视图函数处理完成之后执行。Flask把响应对象传给after_app_request处理程序，以防修改响应。

本例中after_app_request只是获取flak_sqlalchemy记录的查询时间并把运行缓慢的的查询写入日志。

默认情况下，get_debug_queries()函数只在调试模式中可用
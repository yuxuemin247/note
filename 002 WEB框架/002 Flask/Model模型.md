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


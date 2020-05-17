# Flask表单

## 一、原生表单

#### (1) 创建一个模板文件 代码如下

```html
<h2>表单</h2>
<form action="" method="post">
    <p>用户名：<input type="text" name="username" placeholder="请输入用户名"></p>
    <p>密码：<input type="password" name="userpass" placeholder="请输入密码"></p>
    <p><input type="submit" value="submit"></p>
</form>
```

#### (2) 视图函数如下

```python
from flask import reqeuest
# 原生form表单的使用
@app.route('/form1/',methods=['GET','POST'])
def form1():
    if request.method == 'POST':
        username = request.form.get('username')
        userpass = request.form.get('userpass')
        return '用户名为：{} 密码为：{}'.format(username,userpass)
    else:
        return render_template('form1.html')
```

**注意：**

路由请求方式默认为get 所以当有的请求方式进行请求的时候 Method Not Allowed 

更改请求方式

@app.route('/form1/',methods=['GET','POST'])

form表单的action属性值不给默认为提交给当前地址



## 二、flask-wtf表单扩展库

**安装：**

pip install flask-wtf

**说明：**

是一个用于表单处理的扩展库 提供了csrf 表单校验等功能 使用非常的方便

#### 常见字段类型和验证器

#### (1) 字段类型

| 字段类型      | 说明                           |
| ------------- | ------------------------------ |
| StringField   | 普通文本字段                   |
| SubmitField   | 提交按钮                       |
| PasswordField | 密码文本字段                   |
| HiddenField   | 隐藏文本字段                   |
| TextAreaField | 多行文本字段                   |
| DateField     | 文本字段 datetime.date格式     |
| DateTimeField | 文本字段 datetime.datetime格式 |
| IntegerField  | 文本字段 值为整数              |
| FloatField    | 文本字段 值为小数              |
| BooleanField  | 复选框 值为True或者False       |
| RadioField    | 单选框                         |
| SelectField   | 下拉框                         |
| FileField     | 文件上传                       |

#### (2) 常见验证器

| 验证器       | 说明                                  |
| ------------ | ------------------------------------- |
| DateRequired | 必须有值                              |
| Email        | 邮箱地址                              |
| IPAddress    | IP地址                                |
| Length       | 规定字符长度 有max和min俩个值进行限制 |
| NumberRange  | 值的范围                              |
| EqualTo      | 验证俩个字段的一致性                  |
| URL          | 验证有效的URL地址                     |
| Regexp       | 正则验证                              |



#### (3) 简单使用wtf

视图函数代码如下

```python
from flask import Flask,render_template,request
from flask_script import Manager
# 导入表单类的基类
from flask_wtf import FlaskForm
# 导入字段类型
from wtforms import StringField,PasswordField,SubmitField


app = Flask(__name__)
# 用于生成csrf_token值
app.config['SECRET_KEY'] = 'SECRET_KEy'
manager = Manager(app)


# 定义表单类
class Register(FlaskForm):
    # username为name名称 字段类型参数1 为label
    username = StringField('用户名')
    userpass = PasswordField('密码')
    submit = SubmitField('注册')



# 使用表单扩展库 flask-wtf
@app.route('/wtf_form/',methods=['GET','POST'])
def wtf_form():
    # 实例化表单验证器
    form = Register()
    # 提交的方式为POST 并且表单验证器与csrf_token都通过则为真 否则有一个假则为假
    if form.validate_on_submit():
        return '正确'
    return render_template('form2.html',form=form)


if __name__ == '__main__':
    manager.run()
```

模板代码如下

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h2>flask-wtf表单</h2>
<form action="" method="post">
    {{ form.csrf_token }}
    <p>
        {{ form.username.label }} {{ form.username(class='my_username',style="color:blue",placeholder='请输入用户名') }}
        {#  显示验证器验证失败的错误信息 如果没有则为空元祖 否则为列表元素为错误信息  #}
        <span style="color: red">
            {% for err in form.username.errors %}
                {{ err }}
            {% endfor %}
        </span>
    </p>
    <p>
        {{ form.userpass.label }} {{ form.userpass(placeholder='请输入密码') }}
        <span style="color: red">
            {#  显示验证器验证失败的错误信息  #}
            {% for err in form.userpass.errors %}
                {{ err }}
            {% endfor %}
        </span>
    </p>
    <p>{{ form.submit() }}</p>
</form>
</body>
</html>
```

#### 获取表单值

```python
# 提交的方式为POST 并且表单验证器与csrf_token都通过则为真 否则有一个假则为假
    if form.validate_on_submit():
        # 取值
        # 取值方法一 使用请求对象 request
        username = request.form.get('username')
        userpass = request.form.get('userpass')
        # 取值方法二  使用form对象
        username = form.username.data
        userpass = form.userpass.data
        # 获取的为标签
        print(form.username)
        return '用户名为：{} 密码为：{}'.format(username,userpass)
```

#### 使用bootstrap快速渲染

manage.py中bootstrap的代码

```python
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 用于生成csrf_token值
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)
manager = Manager(app)
```

bootstrap的模板表单内容

```html
{% extends 'common/base.html' %}
{% block title %}
    bootstrap快速渲染表单
{% endblock %}
{% from'bootstrap/wtf.html' import quick_form %}
{% block page_content %}
    <h2>Bootstrap快速渲染表单</h2>
    {{ quick_form(form) }}
{% endblock %}
```

#### (4) render_kw属性的使用

```python
info = TextAreaField('个人信息',render_kw={'style':'resize:none','placeholder':'请输入个人信息...'})
```

#### (5) 使用全的字段和验证器

```python
from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
# 导入表单类的父类
from flask_wtf import FlaskForm
# 导入字段
from wtforms import StringField,PasswordField,SubmitField,HiddenField,TextAreaField,DateField,DateTimeField,IntegerField,FloatField,BooleanField,RadioField,SelectField,FileField
# 导入验证器
from wtforms.validators import DataRequired,Email,IPAddress,Length,NumberRange,EqualTo,URL,Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)
manager = Manager(app)

# 定义使用所有的字段和验证器的类
class Form(FlaskForm):
    username = StringField('用户名',validators=[DataRequired('用户名不能为空'),Length(min=6,max=12,message='用户名长度在6~12位之间')])
    userpass = PasswordField('密码',validators=[DataRequired('密码不能为空'),Length(min=6,max=12,message='密码在6~12位之间')])
    confirm = PasswordField('确认密码',validators=[EqualTo('userpass',message='密码和确认密码不一致')])
    uid = HiddenField()
    info = TextAreaField('个人信息',render_kw={'style':'resize:none','placeholder':'请输入个人信息...'})
    date = DateField('日期',format='%Y/%m/%d')
    datetime = DateTimeField('日期时间')
    age = IntegerField('年龄',validators=[NumberRange(min=1,max=99,message='年龄在1~99之间')])
    money = FloatField('工资')
    bool = BooleanField('是否同意以上条款',default='check')
    sex = RadioField('性别',choices=[('m','男'),('w','女')])
    address = SelectField('地址',choices=[('1001','北京'),('1002','上海'),('1003','深圳')])
    photo = FileField('选择头像')
    # 邮箱验证
    email = StringField('邮箱',validators=[Email(message='请输入正确的邮箱')])
    IP = StringField('ip地址',validators=[IPAddress(message='请输入正确的IP地址')])
    url = StringField('url',validators=[URL(message='请输入正确的url地址')])
    phone = StringField('手机号码',validators=[Regexp('^1[3-9]\d{9}$')])
    submit = SubmitField()
```

##### 给字段默认值

```python
@app.route('/wtf_form/',methods=['GET','POST'])
def wtf_form():
    form = Form()
    if form.validate_on_submit():
        return '数据正确'
    # 给隐藏域字段默认值  一定要将默认值的代码放在  form.validate_on_submit()下方
    form.address.data = '1003'
    return render_template('boot_form.html',form=form)
```
#### (6) 自定义表单验证器

```python
# 导入验证器
from wtforms.validators import ValidationError

# 定义使用所有的字段和验证器的类
class Form(FlaskForm):
    username = StringField('用户名',validators=[DataRequired('用户名不能为空'),Length(min=6,max=12,message='用户名长度在6~12位之间')])
    userpass = PasswordField('密码',validators=[DataRequired('密码不能为空'),Length(min=6,max=12,message='密码在6~12位之间')])
    confirm = PasswordField('确认密码',validators=[EqualTo('userpass',message='密码和确认密码不一致')])
    # 自定义表单验证器
    #  实现的功能  如果用户名存在 则提示该用户名已存在
    def validate_username(self,field):
        if field.data == 'lucky_boy':
            raise ValidationError('该用户名已存在 请重新输入...')

    submit = SubmitField()
```



## 三、flash消息显示

#### (1) 概述

当用户请求发出后 用户状态发生了改变 需要给出提示 警告等信息 通常可以通过弹窗给出提示 用户可以根据提示进行下一步的操作  也可以手动取消显示

#### (2) 如何使用

**导入：**

from flask import flash,get_flashed_messages

```python
@app.route('/')
def index():
    flash('lucky老师你好帅啊')
    flash('我好崇拜你啊')
    return render_template('index.html',code=200)
```

模板中

```html
{#  消息闪现的处理  #}
        {% for info in get_flashed_messages() %}
            <div class="alert alert-{% if code == 200 %}success{% else %}warning{% endif %} alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                        aria-hidden="true">&times;</span></button>
                <strong>{{ info }}</strong>
            </div>
        {% endfor %}
```

建议写在base模板中 这样所有子模板都有了消息闪现的功能
## flask-wtf

flask-wtf 是 flask 框架的表单验证模块，可以很方便生成表单。提供了CSRF、字段校验等功能。

- 安装

  ```
  pip install flask-wtf
  ```

- 简单使用

  ```python
  # app.py
  from flask import Flask, request, render_template
  from forms import LoginForm
  
  app = Flask(__name__)
  
  @app.route('/login',methods=['GET','POST'])
  def login():
      form = LoginForm()
      if form.validate_on_submit():  # 验证表单
          if form.username.data == "admin" and form.password.data == '123':
              return 'OK'
            
      return render_template('login.html', form=form)
    
  if __name__ == '__main__':
      app.run(debug=True)
  
  # forms.py
  from flask_wtf import FlaskForm
  from wtforms import StringField
  from wtforms.validators import DataRequired, Length
  
  class LoginForm(FlaskForm):
    	# <input type="text" name="username" id="username" requried>
      # StringField 声明一个普通的 文本输入框
      # label 声明一个 <lable for="username">用户名</lable>
      # validators 声明一组验证器，DataRequired 声明数据不能为空
      username = StringField(label='用户名', validators=[DataRequired(message="用户名不能为空")])
      password = PasswordField(label='密码', validators=[DataRequired()])
  
  # templates/login.html
  <form method="post" action="/loign">
  {{ form.csrf_token }}
  {{ form.username.label }} {{ form.username(size=20) }}
  {{ form.password.label }} {{ form.password }}
  <input type="submit" value="Login">
  </form>
  ```

- 表单定义

  ```python
  # 参数：
  class AdminForm(FlaskForm):
      username = StringField(label='用户名', validators=[DataRequired(),Length(4,20)])
      password_hash = PasswordField(label='密码',validators=[DataRequired(),Length(4,20)])
      limit = SelectField(label='用户权限',
                          choices=[('guest', '所有权限'),
                                   ('operation', '可读可写不可删除'),
                                   ('management', '可读不可写')],
                          default='guest')  # 权限
  
  # 字段一般的参数
  # label:字段的名字
  # default：默认值
  # validators：字段的验证序列
  # description：字段的描述
  # choices：SelectField和他的子类有的字段，选择框，多选一
  ```
  
  
  
- 常用字段

  | 字段类型      | 说明                   |
  | ------------- | --------------------- |
  | StringField   | 普通⽂文本字段         |
  | Submit        | 提交按钮               |
  | PasswordField | 密⽂文字段             |
  | HiddenField   | 隐藏字段               |
  | RadioField    | 单选框                 |
  | BooleanField  | 复选框                 |
  | FileField     | ⽂文件上传             |
  | SelectField   | 下拉框                 |
  | TextAreaField | ⽂文本域               |
  | IntegerField  | ⽂文本字段，值为整数   |
  | FloatField    | ⽂文本字段，值为浮点数 |
  | DateField     | datetime.date类型      |
  | DateTimeField | datetime.datetime类型  |
  
- 常用验证器

  | 验证器器     | 说明                 |
  | ------------ | -------------------- |
  | Length       | 规定字符⻓长度       |
  | DataRequired | 确保字段有值         |
  | Email        | 邮箱地址             |
  | IPAddress    | IP地址               |
  | NumberRange  | 数值的范围           |
  | URL          | 统⼀资源定位符       |
  | EqualTo      | 验证两个字段的一致性 |
  | Regexp       | 正则验证             |

- 自定义表单验证

  ```python
  class MyForm(FlaskForm):
      name = StringField('name', validators=[DataRequired(), Length(4,20)])
      # 自定义验证格式为：validate_字段名
      def validate_name(self, field):
          print(field.data)
          if hasattr(self, 'name') and len(self.name.data) > 5:
              print(self.name.data)
              return True
          raise ValidationError('超过5个字符')
  
  # 在自定义的验证方法中，抛出异常使用 ValidationError，validate 会自动捕捉。
  ```

- 宏定义表单

  ```
  {# 宏定义表单示例 _formhelpers.html 模板 #}
  
  {% macro render_field(field) %}
    <dt>{{ field.label }}
    <dd>{{ field(**kwargs)|safe }}
    {% if field.errors %}
      <ul class=errors>
      {% for error in field.errors %}
        <li>{{ error }}</li>
      {% endfor %}
      </ul>
    {% endif %}
    </dd>
  {% endmacro %}
  ```

  ```
  {# register.html 模板 #}
  
  {% from "_formhelpers.html" import render_field %}
  <form method=post>
    <dl>
      {{ render_field(form.username) }}
      {{ render_field(form.email) }}
      {{ render_field(form.password) }}
      {{ render_field(form.confirm) }}
      {{ render_field(form.accept_tos) }}
    </dl>
    <p><input type=submit value=Register></p>
  </form>
  ```
  
- 在 flask 中 创建、编辑 的用法

  ```python
  # 创建资源
  @app.route('/article/add/', methods=['GET', 'POST'])
  def article_add():
      form = ArticleForm()
  
      if form.validate_on_submit():
          # 通过表单验证后，可以从 form.字段名.data 中获取数据
          title = form.title.data
          content = form.content.data
  
          # 根据获取到的验证后的数据，创建 Article 对象
          article = Article()
          article.title = title
          article.content = content
  
          # 将 Article 对象保存到数据库
          db.session.add(article)
          db.session.commit()
  
          flash('文章保存成功')
          return redirect(url_for('blue.article_list'))
  
      return render_template('article-add.html', form=form)
  
  # 修改资源
  @app.route('/article/<article_id>/change/', methods=['POST', 'GET'])
  def article_change(article_id):
      article = Article.query.get(article_id)
      # 根据 数据库中查询到的数据 创建 Form 对象
      form = ArticleForm(obj=article)
  
      if form.validate_on_submit():
        	# 使用表单对象的 populate_obj 方法，用已验证表单的内容来填充 Article 对象
          form.populate_obj(article)
          db.session.commit()
  
          flash('文章保存成功')
          return redirect(url_for('blue.article_list'))
  
      return render_template('article-change.html', form=form)
  ```

  
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,StopValidation,Email

from app.models import User
class RegisterForm(FlaskForm):
    nickname = StringField(default='',validators=[DataRequired(message='昵称不正确')])
    email =StringField(default='',validators=[Email(message='邮箱不正确') ])
    password =PasswordField(validators=[Length(min=4,max=8,message='密码不正确')])
    password_confirm =PasswordField(validators=([EqualTo('password',message ='输入不一致')]))
    #自定义验证函数格式，validata_字段名
    def validata_nickname(self,field):
        nickname =field.data
        if User.query.filter_by(nickname=nickname).count>0:
            raise ValidationError('昵称已存在')
            # raise  StopValidation('昵称已存在')
    def validata_email(self,field):
        email =field.data
        if User.query.filter_by(email=email).count()>0:
            raise ValidationError('邮箱已存在')

class LoginForm(FlaskForm):
    email = StringField(default='', validators=[Email(message='邮箱不正确')])
    password = PasswordField(validators=[Length(min=4, max=8, message='密码不正确')])

# class ArticleForm(FlaskForm):

from pyramid_wtforms import Form, StringField, PasswordField
from pyramid_wtforms.validators import  InputRequired

class LoginForm(Form):
    name = StringField('帳號', [InputRequired('請輸入帳號')])
    password = PasswordField('密碼', [InputRequired('請輸入密碼')])
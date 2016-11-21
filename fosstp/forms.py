from pyramid_wtforms import Form, StringField, PasswordField
from pyramid_wtforms.validators import InputRequired, Email, EqualTo


class LoginForm(Form):
    name = StringField('帳號', [InputRequired('請輸入帳號')])
    password = PasswordField('密碼', [InputRequired('請輸入密碼')])


class SignupForm(Form):
    name = StringField('帳號', [InputRequired('請輸入帳號')])
    password = PasswordField('密碼', [InputRequired('請輸入密碼')])
    password_confirm = PasswordField('請再次輸入密碼', [InputRequired('請再次輸入密碼'), EqualTo('password', '密碼必須相同')])
    email = StringField('Email', [InputRequired('請輸入 Email'), Email('必須為 Email 格式')])


class SettingsForm(Form):
    old_password = PasswordField('請輸入舊密碼', [InputRequired('請輸入舊密碼')])
    new_password = PasswordField('請輸入新密碼', [InputRequired('請輸入新密碼')])
    new_password_confirm = PasswordField('請再次輸入新密碼', [InputRequired('請再次輸入新密碼'), EqualTo('new_password', '新密碼必須相同')])
    email = StringField('Email', [InputRequired('請輸入 Email'), Email('必須為 Email 格式')])
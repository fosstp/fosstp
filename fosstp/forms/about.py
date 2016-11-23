from pyramid_wtforms import Form, TextAreaField
from pyramid_wtforms.validators import InputRequired


class AboutEditForm(Form):
    content = TextAreaField('內容', [InputRequired('請輸入內容')])
from pyramid_wtforms import Form, StringField, TextAreaField
from pyramid_wtforms.validators import InputRequired


class ForumCategoryAddForm(Form):
    name = StringField('標題', [InputRequired('請輸入標題')])
    description = TextAreaField('說明', [InputRequired('請輸入說明')])
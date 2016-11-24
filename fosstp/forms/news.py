from pyramid_wtforms import Form, StringField, TextAreaField, HiddenField
from pyramid_wtforms.validators import InputRequired, Regexp


class NewsAddForm(Form):
    title = StringField('標題', [InputRequired('請輸入標題')])
    content = TextAreaField('內容', [InputRequired('請輸入內容')])

class NewsForm(NewsAddForm):
    id = HiddenField('id', [Regexp(r'\d+', message='需為正整數')])
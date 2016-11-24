from pyramid_wtforms import Form, StringField, TextAreaField, HiddenField
from pyramid_wtforms.validators import InputRequired, Regexp


class ForumCategoryAddForm(Form):
    name = StringField('標題', [InputRequired('請輸入標題')])
    description = TextAreaField('說明', [InputRequired('請輸入說明')])

class ForumTopicAddForm(Form):
    title = StringField('主題', [InputRequired('請輸入主題')])
    content = TextAreaField('內容', [InputRequired('請輸入內容')])

class ForumTopicForm(ForumTopicAddForm):
    id = HiddenField('id', [Regexp(r'\d+', message='需為正整數')])

class ForumReplyAddForm(Form):
    content = TextAreaField('內容', [InputRequired('請輸入內容')])

class ForumReplyForm(ForumReplyAddForm):
    id = HiddenField('id', [Regexp(r'\d+', message='需為正整數')])
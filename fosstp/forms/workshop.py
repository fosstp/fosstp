from pyramid_wtforms import Form, TextAreaField
from pyramid_wtforms.validators import InputRequired


class WorkshopEditForm(Form):
    link = TextAreaField('Google 日曆內嵌連結', [InputRequired('請輸入Google 日曆內嵌連結')])
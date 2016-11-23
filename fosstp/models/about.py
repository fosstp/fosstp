from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, Text

class AboutModel(BaseObject):
    '''關於本站'''

    __tablename__ = 'about'

    id = Column(Integer, primary_key=True)

    # 內容
    content = Column(Text)
from datetime import datetime
from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime


__all__ = ['NewsModel']

class NewsModel(BaseObject):
    '''最新消息'''

    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)

    # 標題
    title = Column(String(255), nullable=False, default='')

    # 內容
    content = Column(Text, nullable=False, default='')

    # 作者，靠 permission 限制只有 admin 群組才能 po 文章
    user_id = Column(Integer, ForeignKey('users.id'))

    # 建立時間
    create_datetime = Column(DateTime, default=datetime.now)
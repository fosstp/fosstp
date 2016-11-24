from datetime import datetime
from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime


__all__ = ['LinkModel']

class LinkModel(BaseObject):
    '''友站連結'''

    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)

    # 名稱
    name = Column(String(255), nullable=False, default='')

    # 內容
    link = Column(String(255), nullable=False, default='')

    # 作者，靠 permission 限制只有 admin 群組才能 po 連結
    user_id = Column(Integer, ForeignKey('users.id'))

    # 建立時間
    create_datetime = Column(DateTime, default=datetime.now)
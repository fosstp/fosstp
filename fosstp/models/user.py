from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .forum import ForumTopicModel, ForumReplyModel
from .news import NewsModel


__all__ = ['UserModel']

class UserModel(BaseObject):
    '''使用者帳號'''

    __tablename__ = 'users'

    id    = Column(Integer, primary_key=True)

    # 帳號名稱
    name = Column(String(255), nullable=False, unique=True, default='')

    # 密碼
    password = Column(String(255), nullable=False, default='')

    # 群組，若要多值用,隔開。此欄位只有管理者可異動
    group = Column(String(255), nullable=False, default='member')

    # email
    email = Column(String(255), nullable=False, default='')

    # 發表的討論區文章
    forum_topics = relationship(ForumTopicModel, backref='user')

    # 發表的討論區回應
    forum_replies = relationship(ForumReplyModel, backref='user')

    # 發表的最新消息
    news = relationship(NewsModel, backref='user')
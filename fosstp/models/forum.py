from datetime import datetime
from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

__all__ = ['ForumCategoryModel', 'ForumTopicModel', 'ForumReplyModel']

class ForumCategoryModel(BaseObject):
    '''討論區分類，比如程式設計、系統管理等分類'''

    __tablename__ = 'forum_categories'

    id = Column(Integer, primary_key=True)

    # 分類名稱
    name = Column(String(255), nullable=False, default='')

    description = Column(Text, nullable=False, default='')

    topics = relationship('ForumTopicModel', backref='category')

class ForumTopicModel(BaseObject):
    '''討論區每筆討論的主題'''

    __tablename__ = 'forum_topics'

    id = Column(Integer, primary_key=True)

    # 主題
    title = Column(String(255), nullable=False, default='')

    # 內容
    content = Column(Text, nullable=False, default='')

    # 屬於哪個討論區分類
    category_id = Column(Integer, ForeignKey('forum_categories.id'))

    # 作者是誰
    user_id = Column(Integer, ForeignKey('users.id'))

    # 有哪些回文
    forum_replies = relationship('ForumReplyModel', backref='topic')

    # 建立時間
    create_datetime = Column(DateTime, default=datetime.now)

class ForumReplyModel(BaseObject):
    '''討論區每筆回文'''

    __tablename__ = 'forum_replies'

    id = Column(Integer, primary_key=True)

    # 內容
    content = Column(Text, nullable=False, default='')

    # 哪篇主題
    forum_topic_id = Column(Integer, ForeignKey('forum_topics.id'))

    # 作者是誰
    user_id = Column(Integer, ForeignKey('users.id'))

    # 建立時間
    create_datetime = Column(DateTime, default=datetime.now)
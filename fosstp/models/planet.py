from datetime import datetime
from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship


__all__ = ['PlanetModel']

class PlanetModel(BaseObject):
    '''星球聯播'''

    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)

    # 網址
    link = Column(String(255), nullable=False, default='')

    # 作者，靠 permission 限制只有 admin 群組才能 po 連結
    user_id = Column(Integer, ForeignKey('users.id'))

    # 建立時間
    create_datetime = Column(DateTime, default=datetime.now)

    contents = relationship('PlanetContentModel', backref='planet')

class PlanetContentModel(BaseObject):
    '''星球聯播內容'''

    __tablename__ = 'planet_contents'

    id = Column(Integer, primary_key=True)

    # 文章標題
    title = Column(String(255), nullable=False, default='')

    # 文章內容
    content = Column(Text, nullable=False, default='')

    # 文章連結
    link = Column(String(255), nullable=False, default='')

    planet_id = Column(Integer, ForeignKey('planets.id'))
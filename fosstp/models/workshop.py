from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, Text


__all__ = ['WorkshopModel']

class WorkshopModel(BaseObject):
    '''行事曆連結'''

    __tablename__ = 'workshop'

    id = Column(Integer, primary_key=True)

    # 內嵌連結
    link = Column(Text)
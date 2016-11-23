from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, Integer, String

class UserModel(BaseObject):
    '''使用者帳號'''

    __tablename__ = 'users'

    id    = Column(Integer, primary_key=True)

    # 帳號名稱
    name = Column(String(255), nullable=False, unique=True)

    # 密碼
    password = Column(String(255), nullable=False)

    # 群組，若要多值用,隔開。此欄位只有管理者可異動
    group = Column(String(255), nullable=False, default='member')

    # email
    email = Column(String(255), nullable=False)

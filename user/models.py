from bali import db

from sqlalchemy import Integer, Column, String

from core.config import settings

db.connect(settings.SQLALCHEMY_DATABASE_URI)
db.create_all()


class User(db.BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)

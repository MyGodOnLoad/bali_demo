from bali import db

from sqlalchemy import Integer, Column, String

from core.config import settings


db.connect(settings.SQLALCHEMY_DATABASE_URI)
db.create_all()


class Order(db.BaseModel):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    user_id = Column(String)

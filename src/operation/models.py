from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, MetaData, String, Table

from src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    id_telegram = Column(Integer, unique=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    language_code = Column(String)
    is_bot = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)


class Operation(db.Model):
    __tablename__ = "operation"

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    category = db.Column(db.String(length=255))
    kind = db.Column(db.Integer)
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime(), default=func.now())

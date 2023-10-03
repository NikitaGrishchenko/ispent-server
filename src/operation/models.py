import enum
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)

from src.database import Base


class KindOperationEnum(enum.Enum):
    INCOME = 1
    EXPENSE = 2


class Operation(Base):
    __tablename__ = "operation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(255), nullable=False)
    kind = Column(Enum(KindOperationEnum), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now)


# class CategoryUser(db.Model):
#     __tablename__ = "category_user"

#     id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     name = db.Column(db.String(length=255))
#     kind = db.Column(db.Integer)
#     __table_args__ = (db.UniqueConstraint("user_id", "name", "kind", name="_cat_user"),)


# class Operation(db.Model):
#     __tablename__ = "operation"

#     id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     category = db.Column(db.String(length=255))
#     kind = db.Column(db.Integer)
#     amount = db.Column(db.Float)
#     date = db.Column(db.DateTime(), default=func.now())

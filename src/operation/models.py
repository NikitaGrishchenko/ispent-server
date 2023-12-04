from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from src.database import Base

from .enum import KindOperationEnum


class Operation(Base):
    __tablename__ = "operation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    category_user_id = Column(
        Integer, ForeignKey("category_user.id", ondelete="CASCADE"), nullable=False
    )
    category_user = relationship("CategoryUser", lazy="joined")
    kind = Column(Enum(KindOperationEnum), nullable=False)
    comment = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)


class CategoryUser(Base):
    __tablename__ = "category_user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    kind = Column(Enum(KindOperationEnum), nullable=False)
    __table_args__ = (
        UniqueConstraint("user_id", "name", "kind", name="_unique_catagory_user"),
    )
    color = Column(String(255), nullable=False)
    icon = Column(String(255), nullable=False)

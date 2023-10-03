from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)

from src.database import Base
from src.operation.enum import KindOperationEnum


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    id_telegram = Column(Integer, unique=True, nullable=False)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    language_code = Column(String)
    is_bot = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)


class CategoryUser(Base):
    __tablename__ = "category_user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(length=255), nullable=False)
    kind = Column(Enum(KindOperationEnum), nullable=False)
    __table_args__ = (
        UniqueConstraint("user_id", "name", "kind", name="_unique_catagory_user"),
    )

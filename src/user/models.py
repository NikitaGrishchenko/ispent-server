from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
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


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    id_telegram = Column(Integer, unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    language_code = Column(String(255))
    is_bot = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    hashed_password: str = Column(String(1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


class CategoryUser(Base):
    __tablename__ = "category_user"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    kind = Column(Enum(KindOperationEnum), nullable=False)
    __table_args__ = (
        UniqueConstraint("user_id", "name", "kind", name="_unique_catagory_user"),
    )

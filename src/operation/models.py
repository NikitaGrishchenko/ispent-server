from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String

from src.database import Base

from .enum import KindOperationEnum


class Operation(Base):
    __tablename__ = "operation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    category = Column(String(255), nullable=False)
    kind = Column(Enum(KindOperationEnum), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.now)

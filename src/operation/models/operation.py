from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base
from src.operation.enum import KindOperationEnum


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

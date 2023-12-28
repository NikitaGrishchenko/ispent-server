from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint

from src.database import Base
from src.operation.enum import KindOperationEnum


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

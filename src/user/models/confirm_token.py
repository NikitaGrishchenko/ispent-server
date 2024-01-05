from sqlalchemy import Column, Enum, ForeignKey, Integer, String, UniqueConstraint

from src.core.database import Base


class ConfirmToken(Base):
    __tablename__ = "confirm_token"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    token = Column(String(255), nullable=False)

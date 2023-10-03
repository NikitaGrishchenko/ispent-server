from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Table

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

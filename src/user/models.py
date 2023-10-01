from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, MetaData, String, Table

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, unique=True),
    Column("id_telegram", Integer, nullable=False, unique=True),
    Column("username", String(255)),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("language_code", String(20)),
    Column("is_bot", Boolean, default=False),
    Column("created_at", DateTime, default=datetime.now),
)

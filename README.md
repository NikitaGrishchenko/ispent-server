ispent-backend

poetry run uvicorn src.core:app --reload

poetry run alembic init migrations
poetry run alembic revision --autogenerate -m "init"
poetry run alembic upgrade head

после создания приложения прописать пути для alembic models в migrations/env.py
from src.user.models import User

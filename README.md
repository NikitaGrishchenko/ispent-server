ispent-backend

uvicorn src.main:app --reload

alembic init migrations
alembic revision --autogenerate -m "Initial models"
alembic upgrade head

1 Доход 
0 Расход


после создания приложения прописать пути для alembic models в migrations/env.py
from src.user.models import User

и для роутеров в main.py
app.include_router(user_router, prefix="/user", tags=["user"])
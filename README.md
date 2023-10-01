ispent-backend

uvicorn src.main:app --reload

alembic init migrations
alembic revision --autogenerate -m "User table"
alembic upgrade 816252f76c81

1 Доход 
0 Расход

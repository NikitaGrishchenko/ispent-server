from fastapi import FastAPI

from src.operation.router import router as operation_router
from src.user.router import router as user_router

app = FastAPI(title="ispent")


app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(operation_router, prefix="/operation", tags=["operation"])

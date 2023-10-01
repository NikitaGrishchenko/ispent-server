from fastapi import FastAPI

from src.user.router import router as user_router

app = FastAPI(title="ispent")


app.include_router(user_router, prefix="/user", tags=["user"])

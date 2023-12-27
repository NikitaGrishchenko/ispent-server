from fastapi import APIRouter

from src.user.v1.router import user_v1_router

api_v1_router = APIRouter()
api_v1_router.include_router(user_v1_router, prefix="/user", tags=("user",))

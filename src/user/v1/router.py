from fastapi import APIRouter

from .views import router

user_v1_router = APIRouter()

user_v1_router.include_router(router)

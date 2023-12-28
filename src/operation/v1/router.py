from fastapi import APIRouter

from .views import router

operation_v1_router = APIRouter()

operation_v1_router.include_router(router)

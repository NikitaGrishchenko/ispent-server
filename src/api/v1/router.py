from fastapi import APIRouter

from src.user.auth import auth_backend, fastapi_users
from src.user.schemas import UserCreate, UserRead
from src.user.v1.router import user_v1_router

api_v1_router = APIRouter()

api_v1_router.include_router(user_v1_router, prefix="/user", tags=["user"])

api_v1_router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
)
api_v1_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.operation.router import router as operation_router

# from app.schemas import UserCreate, UserRead, UserUpdate
from src.user.auth import auth_backend, current_active_user, fastapi_users
from src.user.models import User
from src.user.router import router as user_router
from src.user.schemas import UserCreate, UserRead, UserUpdate

app = FastAPI(title="ispent")

origins = [
    "http://localhost",
    "http://localhost:9000",
    "http://127.0.0.1",
    "http://127.0.0.1:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(operation_router, prefix="/operation", tags=["operation"])

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth", tags=["auth"]
)
app.include_router(
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

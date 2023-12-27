# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from src.operation.router import router as operation_router

# # from app.schemas import UserCreate, UserRead, UserUpdate
# from src.user.auth import auth_backend, current_active_user, fastapi_users
# from src.user.models import User

# # from src.user.router import router as user_router
# from src.user.schemas import UserCreate, UserRead, UserUpdate

# app = FastAPI(title="ispent")

# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# app.include_router(user_router, prefix="/api/user", tags=["user"])
# app.include_router(operation_router, prefix="/api/operation", tags=["operation"])

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)

from src.core.config import SECRET

from .manager import get_user_manager
from .models import User

cookie_transport = CookieTransport(
    cookie_max_age=2500000,
    cookie_name="ispent-jwt",
    cookie_samesite="lax",
    cookie_secure=False,
    cookie_httponly=False,
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=2500000)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)

from fastapi import APIRouter

from src.api_v1.users.auth.backend import auth_backend
from src.api_v1.users.auth.routers import fastapi_users
from src.api_v1.users.schemas import UserRead, UserCreate, UserUpdate

# /login
# /logout
auth_router = APIRouter(tags=['Auth'])
auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

# /register
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

# /request-verify-token
# /verify
auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
auth_router.include_router(
    fastapi_users.get_reset_password_router(),
)

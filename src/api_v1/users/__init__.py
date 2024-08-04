from fastapi import APIRouter

from src.api_v1.users.auth.routers import fastapi_users
from src.api_v1.users.schemas import UserRead, UserUpdate

# /login
# /logout
users_router = APIRouter(tags=['Users'])

# /me
# /id
users_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)

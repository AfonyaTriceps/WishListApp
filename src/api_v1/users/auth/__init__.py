from fastapi import APIRouter

from src.api_v1.users.auth.backend import auth_backend
from src.api_v1.users.auth.routers import fastapi_users

auth_router = APIRouter(tags=['Auth'])
auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)

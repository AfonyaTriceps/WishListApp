from fastapi import APIRouter

from src.api_v1.users import users_router
from src.api_v1.users.auth import auth_router
from src.api_v1.wishes.views import wishes_router

router = APIRouter()
router.include_router(router=wishes_router, prefix='/wishes')
router.include_router(router=auth_router, prefix='/auth')
router.include_router(router=users_router, prefix='/users')

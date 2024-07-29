from fastapi import APIRouter

from src.api_v1.wishes.views import wishes_router

router = APIRouter()
router.include_router(router=wishes_router, prefix='/wishes')

from fastapi import FastAPI

from src import router
from src.api_v1.settings import settings

app = FastAPI(title='WishList')
app.include_router(router=router, prefix=settings.api_v1_prefix)

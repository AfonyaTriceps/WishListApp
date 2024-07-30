from typing import TYPE_CHECKING

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.users.auth.user_manager import UserManager
from src.api_v1.db.db_helper import async_session
from src.api_v1.users.models import User
from src.api_v1.users.auth.models import AccessToken

if TYPE_CHECKING:
    from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase


async def get_access_token_db(
    session: AsyncSession = Depends(async_session),
):
    yield AccessToken.get_db(session=session)


async def get_user_db(session: AsyncSession = Depends(async_session)):
    yield User.get_db(session=session)


async def get_user_manager(users_db: 'SQLAlchemyUserDatabase' = Depends(get_user_db)):
    yield UserManager(users_db)

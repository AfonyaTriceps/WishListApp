from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from src.api_v1.db.db_helper import async_session
from src.api_v1.users.models import User
from src.api_v1.auth.models import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


def get_database_strategy(
    access_token_db: AccessTokenDatabase['AccessToken'] = Depends(async_session),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


async def get_user_db(session: AsyncSession = Depends(async_session)):
    yield User.get_db(session=session)


async def get_access_token_db(
    session: AsyncSession = Depends(async_session),
):
    yield AccessToken.get_db(session=session)

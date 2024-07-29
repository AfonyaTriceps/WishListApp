from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from sqlalchemy.ext.asyncio import AsyncSession
from src.api_v1.db.db_helper import async_session

if TYPE_CHECKING:
    from src.api_v1.auth.models import AccessToken
    from src.api_v1.users.models import User


async def get_access_token_db(
    session: AsyncSession = Depends(async_session),
):
    yield AccessToken.get_db(session=session)


async def get_user_db(session: AsyncSession = Depends(async_session)):
    yield User.get_db(session=session)


def get_database_strategy(
    access_token_db: AccessTokenDatabase['AccessToken'] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)

from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.authentication.strategy import AccessTokenDatabase, DatabaseStrategy

from src.api_v1.auth.dependencies import get_access_token_db

if TYPE_CHECKING:
    from src.api_v1.auth.models import AccessToken


def get_database_strategy(
    access_token_db: AccessTokenDatabase['AccessToken'] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)

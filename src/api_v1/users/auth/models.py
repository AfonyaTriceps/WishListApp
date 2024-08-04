from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase, SQLAlchemyBaseAccessTokenTable)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from src.api_v1.db import Base


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[int]):
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    @classmethod
    def get_db(cls, session: 'AsyncSession') -> SQLAlchemyAccessTokenDatabase:
        """Получение БД для токена."""
        return SQLAlchemyAccessTokenDatabase(session, cls)

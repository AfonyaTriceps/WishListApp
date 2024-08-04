from datetime import datetime
from typing import TYPE_CHECKING, Optional

from fastapi_users_db_sqlalchemy import (SQLAlchemyBaseUserTable,
                                         SQLAlchemyUserDatabase)
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.api_v1.db import Base
from src.api_v1.utils.mixins import IdPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.api_v1.wishes.models import WishCard


class User(Base, IdPkMixin, SQLAlchemyBaseUserTable[int]):
    """Модель карточки пользователя."""

    username: Mapped[str] = mapped_column(String(50), unique=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(30))
    last_name: Mapped[Optional[str]] = mapped_column(String(60))
    birth_date: Mapped[Optional[datetime]]

    wishes: Mapped[list['WishCard']] = relationship('WishCard', back_populates='user', cascade='all, delete-orphan')

    @classmethod
    def get_db(cls, session: 'AsyncSession') -> SQLAlchemyUserDatabase:
        """Получение БД пользователя."""
        return SQLAlchemyUserDatabase(session, cls)

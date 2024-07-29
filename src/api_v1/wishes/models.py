from typing import TYPE_CHECKING, Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.api_v1.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from src.api_v1.utils.mixins import IdPkMixin

if TYPE_CHECKING:
    from src.api_v1.users.models import User
    from sqlalchemy.ext.asyncio import AsyncSession


class WishCard(Base, IdPkMixin):
    """Модель карточки желания."""
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    price: Mapped[Optional[float]]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
    photo: Mapped[Optional[str]]
    user: Mapped['User'] = relationship('User', back_populates='wishes')

    @classmethod
    def get_db(cls, session: 'AsyncSession'):
        return SQLAlchemyUserDatabase(session, User)


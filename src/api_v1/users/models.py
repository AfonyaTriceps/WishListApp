from typing import TYPE_CHECKING, Optional
from src.api_v1.db import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum
from src.api_v1.users.constants import Gender
from fastapi_users.db import SQLAlchemyBaseUserTable

from src.api_v1.utils.mixins import IdPkMixin

if TYPE_CHECKING:
    from src.api_v1.wishes.models import WishCard


class User(Base, IdPkMixin, SQLAlchemyBaseUserTable[int]):
    """Модель карточки пользователя."""
    username: Mapped[str] = mapped_column(String(50), unique=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(30))
    last_name: Mapped[Optional[str]] = mapped_column(String(60))
    birth_date: Mapped[Optional[datetime]]
    gender: Mapped[str] = mapped_column(Enum(Gender))

    wishes: Mapped[list['WishCard']] = relationship('WishCard', back_populates='user', cascade='all, delete-orphan')

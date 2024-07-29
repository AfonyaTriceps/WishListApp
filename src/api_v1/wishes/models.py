from typing import TYPE_CHECKING, Optional
from src.api_v1.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer

from src.api_v1.utils.mixins import IdPkMixin

if TYPE_CHECKING:
    from src.api_v1.users.models import User


class WishCard(Base, IdPkMixin):
    """Модель карточки желания."""
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    price: Mapped[Optional[float]]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    photo: Mapped[Optional[str]]
    user: Mapped['User'] = relationship('User', back_populates='wishes')


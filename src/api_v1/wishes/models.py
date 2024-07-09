from src.api_v1.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from typing import Optional


class WishCard(Base):
    """Модель карточки желания."""
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    price: Mapped[Optional[float]]
    photo: Mapped[Optional[bytes]]
    #user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'))

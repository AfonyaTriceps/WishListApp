from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column


class IdPkMixin:
    """Миксин с id для таблиц."""

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

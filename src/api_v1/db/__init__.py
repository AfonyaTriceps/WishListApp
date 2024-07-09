from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from sqlalchemy import Integer


class Base(DeclarativeBase):
    """Базовый класс моделей."""
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

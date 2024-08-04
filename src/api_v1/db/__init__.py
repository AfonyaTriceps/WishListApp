from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Базовый класс моделей."""

    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        """Имя таблицы."""
        return f'{cls.__name__.lower()}s'

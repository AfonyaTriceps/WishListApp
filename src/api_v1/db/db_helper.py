from collections.abc import AsyncGenerator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)

from src.api_v1.settings import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Генератор сессий.

        yield: сессия

        Raise:
            SQLAlchemyError: если произошла ошибка при подключении или при работе с базой данных
        """
        async with self.session() as session:
            try:
                yield session
                await session.commit()
            except SQLAlchemyError as error:
                await session.rollback()
                raise SQLAlchemyError(error)


db_helper = DatabaseHelper(url=settings.db_url, echo=True)
async_session = db_helper.session_dependency

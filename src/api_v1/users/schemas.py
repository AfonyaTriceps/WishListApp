import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Схема для получения пользователя."""

    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class UserCreate(schemas.BaseUserCreate):
    """Схема для создания пользователя."""

    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class UserUpdate(schemas.BaseUserUpdate):
    """Схема для обновления пользователя."""

    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    birth_date: Optional[datetime.date]

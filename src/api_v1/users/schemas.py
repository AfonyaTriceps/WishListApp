import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class UserCreate(schemas.BaseUserCreate):
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    birth_date: Optional[datetime.date]

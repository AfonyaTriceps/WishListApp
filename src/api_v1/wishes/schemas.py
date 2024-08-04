from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class BaseWish(BaseModel):
    """Базовая схема желания."""

    model_config = ConfigDict(from_attributes=True)

    name: str
    url: Optional[HttpUrl]
    description: Optional[str]
    price: Optional[float]


class Wish(BaseWish):
    """Базовая схема с id желания."""

    id: int


class CreateWish(BaseWish):
    """Cхема для создания желания."""

    pass


class UpdateWish(CreateWish):
    """Схема для обновления желания."""

    name: Optional[str]

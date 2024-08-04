from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class BaseWish(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    url: Optional[HttpUrl]
    description: Optional[str]
    price: Optional[float]


class Wish(BaseWish):
    id: int


class CreateWish(BaseWish):
    pass


class UpdateWish(CreateWish):
    name: Optional[str]

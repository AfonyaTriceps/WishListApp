from typing import Optional

from pydantic import BaseModel, ConfigDict


class BaseWish(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    url: Optional[str]
    description: Optional[str]
    price: Optional[float]
    photo: Optional[str]
    user_id: int


class Wish(BaseWish):
    id: int


class CreateWish(Wish):
    pass


class UpdateWish(CreateWish):
    name: Optional[str]

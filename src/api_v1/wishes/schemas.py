from pydantic import BaseModel, ConfigDict


class BaseWish(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    url: str
    description: str
    price: float
    photo: bytes


class Wish(BaseWish):
    id: int


class CreateWish(Wish):
    pass


class UpdateWish(CreateWish):
    pass

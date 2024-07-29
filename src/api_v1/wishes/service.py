from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.api_v1.wishes.models import WishCard
from src.api_v1.wishes.schemas import CreateWish, UpdateWish


async def get_wishes(session: AsyncSession) -> list[WishCard]:
    wishes_query = await session.execute(select(WishCard).options(joinedload(WishCard.user)).order_by(WishCard.id))
    wishes = wishes_query.scalars().all()

    return list(wishes)


async def get_wish(session: AsyncSession, wish_id: int) -> WishCard | None:
    return await session.get(WishCard, wish_id)


async def create_wish(session: AsyncSession, create_schema: CreateWish) -> WishCard:
    new_wish = WishCard(**create_schema.model_dump())
    session.add(new_wish)
    await session.commit()
    await session.refresh(new_wish)

    return new_wish


async def update_wish(session: AsyncSession, wish: WishCard, wish_update: UpdateWish) -> WishCard:
    for key, value in wish_update.model_dump().items():
        setattr(wish, key, value)

    await session.commit()
    return wish


async def delete_wish(session: AsyncSession, wish: WishCard) -> None:
    await session.delete(wish)
    await session.commit()

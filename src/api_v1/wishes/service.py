from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.api_v1.wishes.models import WishCard
from src.api_v1.wishes.schemas import CreateWish


async def get_wishes(session: AsyncSession) -> list[WishCard]:
    wishes_query = await session.execute(select(WishCard).order_by(WishCard.id))
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

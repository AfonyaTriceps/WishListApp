from typing import TYPE_CHECKING

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api_v1.wishes.models import WishCard
from src.api_v1.wishes.schemas import CreateWish, UpdateWish

if TYPE_CHECKING:
    from src.api_v1.users.models import User


async def get_wishes(session: AsyncSession, user: 'User') -> list[WishCard]:
    """Получение списка желаний."""
    wishes_query = await session.execute(select(WishCard).where(WishCard.user_id == user.id).order_by(WishCard.id))
    wishes = wishes_query.scalars().all()

    return list(wishes)


async def get_wish(session: AsyncSession, wish_id: int, user: 'User') -> WishCard | None:
    """Получение желания по id."""
    wish_query = await session.execute(select(WishCard).where(WishCard.user_id == user.id, WishCard.id == wish_id))
    wish = wish_query.scalar_one_or_none()
    return wish


async def create_wish(session: AsyncSession, create_schema: CreateWish, user: 'User') -> WishCard:
    """Создание желания."""
    new_wish = WishCard(**create_schema.model_dump())
    new_wish.user_id = user.id
    new_wish.url = str(new_wish.url) if new_wish.url else None
    session.add(new_wish)
    await session.commit()
    await session.refresh(new_wish)

    return new_wish


async def update_wish(session: AsyncSession, wish: WishCard, wish_update: UpdateWish) -> WishCard:
    """Обнорвление желания."""
    for key, value in wish_update.model_dump().items():
        setattr(wish, key, value)

    await session.commit()
    return wish


async def delete_wish(session: AsyncSession, wish: WishCard) -> None:
    """Удаление желания."""
    await session.delete(wish)
    await session.commit()

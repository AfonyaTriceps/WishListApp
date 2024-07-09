from fastapi import APIRouter, HTTPException, status, Depends
from src.api_v1.wishes import service
from src.api_v1.wishes.schemas import CreateWish, Wish, UpdateWish
from sqlalchemy.ext.asyncio import AsyncSession
from src.api_v1.db.db_helper import async_session


wishes_router = APIRouter(tags=['Wishes'])


@wishes_router.get('/', response_model=list[Wish])
async def get_wishes(session: AsyncSession = Depends(async_session)):
    return await service.get_wishes(session=session)


@wishes_router.get('/{wish_id}/', response_model=Wish)
async def get_wish(wish_id: int, session: AsyncSession = Depends(async_session)):
    wish = await service.get_wish(session=session, wish_id=wish_id)
    if wish:
        return wish

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'Продукта с id={wish_id} не существует.'
    )


@wishes_router.post('/', response_model=Wish)
async def create_wish(create_schema: CreateWish, session: AsyncSession = Depends(async_session)):
    return await service.create_wish(session=session, create_schema=create_schema)


@wishes_router.delete('/{wish_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_wish(wish_id: int, session: AsyncSession = Depends(async_session)):
    wish = await service.get_wish(session=session, wish_id=wish_id)
    await service.delete_wish(session=session, wish=wish)


@wishes_router.put('/{wish_id}/', response_model=UpdateWish)
async def update_wish(wish_id: int, wish_update: UpdateWish, session: AsyncSession = Depends(async_session)):
    wish = await service.get_wish(session=session, wish_id=wish_id)
    if not wish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Продукта с id={wish_id} не существует.'
        )

    return await service.update_wish(session=session, wish=wish, wish_update=wish_update)

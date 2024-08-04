from typing import TYPE_CHECKING

from fastapi import HTTPException, status, Depends
from fastapi.responses import StreamingResponse

from src.api_v1.users.auth.routers import current_user
from src.api_v1.wishes import service, wishes_router
from src.api_v1.wishes.schemas import CreateWish, Wish, UpdateWish
from sqlalchemy.ext.asyncio import AsyncSession
from src.api_v1.db.db_helper import async_session
from src.api_v1.wishes.utils import generate_csv

if TYPE_CHECKING:
    from src.api_v1.users.models import User


@wishes_router.get('/', response_model=list[Wish])
async def get_wishes(session: AsyncSession = Depends(async_session), user: 'User' = Depends(current_user)):
    return await service.get_wishes(session=session, user=user)


@wishes_router.get('/{wish_id}/', response_model=Wish)
async def get_wish(wish_id: int, session: AsyncSession = Depends(async_session), user: 'User' = Depends(current_user)):
    wish = await service.get_wish(session=session, wish_id=wish_id, user=user)
    if wish:
        return wish

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'Продукта с id={wish_id} не существует.'
    )


@wishes_router.post('/', response_model=Wish)
async def create_wish(create_schema: CreateWish, session: AsyncSession = Depends(async_session), user: 'User' =
                      Depends(current_user)):
    return await service.create_wish(session=session, create_schema=create_schema, user=user)


@wishes_router.delete('/{wish_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_wish(
        wish_id: int, session: AsyncSession = Depends(async_session), user: 'User' = Depends(current_user)):
    wish = await service.get_wish(session=session, wish_id=wish_id, user=user)
    if not wish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Продукта с id={wish_id} не существует.'
        )
    await service.delete_wish(session=session, wish=wish)


@wishes_router.put('/{wish_id}/', response_model=UpdateWish)
async def update_wish(wish_id: int, wish_update: UpdateWish, session: AsyncSession = Depends(async_session),
                      user: 'User' = Depends(current_user)):
    wish = await service.get_wish(session=session, wish_id=wish_id, user=user)
    if not wish:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Продукта с id={wish_id} не существует.'
        )

    return await service.update_wish(session=session, wish=wish, wish_update=wish_update)


@wishes_router.get('/{wish_id}/download_wishes')
async def get_wishes_in_pdf(session: AsyncSession = Depends(async_session), user: 'User' = Depends(current_user)):
    wishes = await get_wishes(session=session, user=user)
    if not wishes:
        raise HTTPException(status_code=404, detail='Желаний не найдено')
    csv_data = await generate_csv(wishes)
    response = StreamingResponse(
        iter([csv_data]),
        media_type='text/csv'
    )
    response.headers['Content-Disposition'] = 'attachment; filename=wishes.csv'
    return response

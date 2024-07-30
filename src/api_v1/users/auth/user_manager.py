import logging

from typing import Optional, TYPE_CHECKING

from fastapi_users import BaseUserManager, IntegerIDMixin

from src.api_v1.users.models import User
from src.api_v1.settings import settings

if TYPE_CHECKING:
    from fastapi import Request

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.RESET_PASSWORD_TOKEN_SECRET
    verification_token_secret = settings.VERIFICATION_TOKEN_SECRET

    async def on_after_register(self, user: User, request: Optional['Request'] = None):
        log.warning('Пользователь %r зарегистрирован.', user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional['Request'] = None
    ):
        log.warning('Пользователь %r забыл свой пароль. Токен восстановления: %r', user.id, token)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional['Request'] = None
    ):
        log.warning('Требуется подтверждение пользователя %r. Токен подтверждения: %r', user.id, token)

from fastapi_users.authentication import AuthenticationBackend

from fastapi_users.authentication import BearerTransport

from src.api_v1.settings import settings
from src.api_v1.users.auth.strategy import get_database_strategy

bearer_transport = BearerTransport(tokenUrl=settings.auth_prefix)

auth_backend = AuthenticationBackend(
    name='access-token',
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)

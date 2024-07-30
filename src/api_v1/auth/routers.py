from fastapi_users import FastAPIUsers

from src.api_v1.auth.backend import auth_backend
from src.api_v1.auth.dependencies import get_user_manager
from src.api_v1.users.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

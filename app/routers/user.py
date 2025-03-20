from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTStrategy
from app.models.user import User, UserCreate, UserUpdate, UserDB
from app.services.user import get_user_manager
from app.core.config import SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


fastapi_users = FastAPIUsers[User, UserCreate, UserUpdate, UserDB](
    get_user_manager,
    [get_jwt_strategy()],
)

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(get_jwt_strategy()),
    prefix="/auth/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)

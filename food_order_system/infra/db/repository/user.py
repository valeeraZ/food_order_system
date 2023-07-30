from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from food_order_system.infra.db.dependencies import get_db_session
from food_order_system.infra.db.model.user_dto import UserDTO
from food_order_system.infra.db.repository.base import BaseRepository


class UserRepository(BaseRepository[UserDTO]):
    pass


def get_user_repository(
    session: AsyncSession = Depends(get_db_session),
) -> UserRepository:
    return UserRepository(UserDTO, session)

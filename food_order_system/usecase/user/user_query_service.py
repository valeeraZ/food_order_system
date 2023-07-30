from fastapi import Depends

from food_order_system.exception.base_exception import NotFoundException
from food_order_system.infra.db.repository.user import (
    UserRepository,
    get_user_repository,
)
from food_order_system.usecase.user.user_query_model import UserReadModel


class UserQuery:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def find_user_by_phone_number(self, phone_number: str) -> UserReadModel:
        if user_dto := await self.user_repository.get(phone_number=phone_number):
            return UserReadModel.from_orm(user_dto)
        raise NotFoundException(name=f"User with phone number {phone_number}")


def get_user_query_service(
    user_repository: UserRepository = Depends(get_user_repository),
) -> UserQuery:
    return UserQuery(user_repository)

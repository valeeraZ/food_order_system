from food_order_system.domain.user.user_exception import UserNotFoundException
from food_order_system.infra.db.repository.user import UserRepository
from food_order_system.usecase.user.user_query_model import UserReadModel


class UserQuery:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def find_user_by_phone_number(self, phone_number: str) -> UserReadModel:
        if user_dto := await self.user_repository.get(phone_number=phone_number):
            return UserReadModel.from_orm(user_dto)
        raise UserNotFoundException(phone_number=phone_number)

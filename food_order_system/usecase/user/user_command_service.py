import dataclasses

from food_order_system.domain.user.user import User
from food_order_system.infra.db.repository.user import UserRepository
from food_order_system.usecase.user.user_command_model import UserCreateModel
from food_order_system.usecase.user.user_query_model import UserReadModel


class UserCommand:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_create_model: UserCreateModel) -> UserReadModel:
        if user_dto := await self.user_repository.get(
            phone_number=user_create_model.phone_number,
        ):
            return UserReadModel.from_orm(user_dto)
        user = User(**user_create_model.dict())
        user.authenticate_sending_sms()
        user_dto = await self.user_repository.create(
            dataclasses.asdict(user),
        )
        return UserReadModel.from_orm(user_dto)

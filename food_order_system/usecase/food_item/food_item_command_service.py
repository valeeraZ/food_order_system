from fastapi import Depends

from food_order_system.exception.base_exception import NotFoundException
from food_order_system.infra.db.repository.food_item import (
    FoodItemRepository,
    get_food_item_repository,
)
from food_order_system.usecase.food_item.food_item_command_model import (
    FoodItemCreateModel,
    FoodItemUpdateModel,
)
from food_order_system.usecase.food_item.food_item_query_model import FoodItemReadModel


class FoodItemCommand:
    def __init__(self, food_item_repository: FoodItemRepository):
        self.food_item_repository = food_item_repository

    async def create_food_item(
        self,
        food_item_create_model: FoodItemCreateModel,
    ) -> FoodItemReadModel:
        if food_item_dto := await self.food_item_repository.get(
            name=food_item_create_model.name,
        ):
            return FoodItemReadModel.from_orm(food_item_dto)
        food_item_dto = await self.food_item_repository.create(
            food_item_create_model.dict(),
        )
        return FoodItemReadModel.from_orm(food_item_dto)

    async def update_food_item(
        self,
        id: int,
        food_item_update_model: FoodItemUpdateModel,
    ) -> FoodItemReadModel:
        if food_item_dto := await self.food_item_repository.get(
            id=id,
        ):
            food_item_dto = await self.food_item_repository.update_with_dict(
                obj_in=food_item_dto,
                updated_data=food_item_update_model.dict(exclude_unset=True),
            )
            return FoodItemReadModel.from_orm(food_item_dto)
        raise NotFoundException(name=f"Food item with id {id}")


def get_food_item_command_service(
    food_item_repository: FoodItemRepository = Depends(get_food_item_repository),
) -> FoodItemCommand:
    return FoodItemCommand(food_item_repository)

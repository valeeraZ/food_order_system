from fastapi import Depends

from food_order_system.exception.base_exception import NotFoundException
from food_order_system.infra.db.repository.food_item import (
    FoodItemRepository,
    get_food_item_repository,
)
from food_order_system.usecase.food_item.food_item_query_model import FoodItemReadModel


class FoodItemQuery:
    def __init__(self, food_item_repository: FoodItemRepository):
        self.food_item_repository = food_item_repository

    async def find_food_item_by_id(self, id: int) -> FoodItemReadModel:
        if food_item_dto := await self.food_item_repository.get(id=id):
            return FoodItemReadModel.from_orm(food_item_dto)
        raise NotFoundException(name=f"Food item with id {id}")

    async def find_food_item_by_name(self, name: str) -> FoodItemReadModel:
        if food_item_dto := await self.food_item_repository.get(name=name):
            return FoodItemReadModel.from_orm(food_item_dto)
        raise NotFoundException(name=f"Food item with name {name}")


def get_food_item_query_service(
    food_item_repository: FoodItemRepository = Depends(get_food_item_repository),
) -> FoodItemQuery:
    return FoodItemQuery(food_item_repository)

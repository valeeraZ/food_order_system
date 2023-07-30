from fastapi import Depends

from food_order_system.exception.base_exception import NotFoundException
from food_order_system.infra.db.repository.food_category import (
    FoodCategoryRepository,
    get_food_category_repository,
)
from food_order_system.usecase.food_category.food_category_query_model import (
    FoodCategoryReadModel,
)
from food_order_system.usecase.food_item.food_item_query_model import FoodItemReadModel


class FoodCategoryQuery:
    def __init__(self, food_category_repository: FoodCategoryRepository):
        self.food_category_repository = food_category_repository

    async def find_food_category_by_name(self, name: str) -> FoodCategoryReadModel:
        if food_category_dto := await self.food_category_repository.get(name=name):
            return FoodCategoryReadModel.from_orm(food_category_dto)
        raise NotFoundException(name=f"Food category with name {name}")

    async def find_food_items_by_category_name(
        self,
        name: str,
    ) -> list[FoodItemReadModel]:
        if food_category_dto := await self.food_category_repository.get(name=name):
            return [
                FoodItemReadModel.from_orm(food_item_dto)
                for food_item_dto in food_category_dto.food_items
            ]
        raise NotFoundException(name=f"Food category with name {name}")


def get_food_category_query_service(
    food_category_repository: FoodCategoryRepository = Depends(
        get_food_category_repository,
    ),
) -> FoodCategoryQuery:
    return FoodCategoryQuery(food_category_repository)

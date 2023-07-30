from fastapi import Depends

from food_order_system.exception.base_exception import (
    NotCreatedException,
    NotFoundException,
)
from food_order_system.infra.db.repository.food_category import (
    FoodCategoryRepository,
    get_food_category_repository,
)
from food_order_system.usecase.food_category.food_category_command_model import (
    FoodCategoryCreateModel,
)
from food_order_system.usecase.food_category.food_category_query_model import (
    FoodCategoryReadModel,
)
from food_order_system.usecase.food_item.food_item_command_model import (
    FoodItemCreateModel,
)
from food_order_system.usecase.food_item.food_item_command_service import (
    FoodItemCommand,
    get_food_item_command_service,
)
from food_order_system.usecase.food_item.food_item_query_model import FoodItemReadModel


class FoodCategoryCommand:
    def __init__(
        self,
        food_category_repository: FoodCategoryRepository,
        food_item_command: FoodItemCommand,
    ):
        self.food_category_repository = food_category_repository
        self.food_item_command = food_item_command

    async def create_food_category(
        self,
        food_category_create_model: FoodCategoryCreateModel,
    ) -> FoodCategoryReadModel:
        if food_category_dto := await self.food_category_repository.get(
            name=food_category_create_model.name,
        ):
            return FoodCategoryReadModel.from_orm(food_category_dto)
        food_category_dto = await self.food_category_repository.create(
            food_category_create_model.dict(),
        )
        return FoodCategoryReadModel.from_orm(food_category_dto)

    async def create_food_items_under_category(
        self,
        name: str,
        food_items: list[FoodItemCreateModel],
    ) -> list[FoodItemReadModel]:
        if food_category_dto := await self.food_category_repository.get(name=name):
            food_items_created = []
            for food_item in food_items:
                if food_item.category_id != food_category_dto.id:
                    raise NotCreatedException(
                        name=food_item.name,
                        error=f"Wrong category id {food_item.category_id} for food item {food_item.name}",
                    )
                food_items_created.append(
                    await self.food_item_command.create_food_item(food_item),
                )
            return food_items_created
        raise NotFoundException(name=f"Food category with name {name}")


def get_food_category_command_service(
    food_category_repository: FoodCategoryRepository = Depends(
        get_food_category_repository,
    ),
    food_item_command: FoodItemCommand = Depends(get_food_item_command_service),
) -> FoodCategoryCommand:
    return FoodCategoryCommand(food_category_repository, food_item_command)

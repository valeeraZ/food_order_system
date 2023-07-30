from fastapi import APIRouter, Depends, status

from food_order_system.usecase.food_category.food_category_command_model import (
    FoodCategoryCreateModel,
)
from food_order_system.usecase.food_category.food_category_command_service import (
    FoodCategoryCommand,
    get_food_category_command_service,
)
from food_order_system.usecase.food_category.food_category_query_model import (
    FoodCategoryReadModel,
)
from food_order_system.usecase.food_category.food_category_query_service import (
    FoodCategoryQuery,
    get_food_category_query_service,
)
from food_order_system.usecase.food_item.food_item_command_model import (
    FoodItemCreateModel,
)
from food_order_system.usecase.food_item.food_item_query_model import FoodItemReadModel

router = APIRouter(prefix="/food_categories", tags=["food categories"])


@router.post(
    "/",
    response_model=FoodCategoryReadModel,
    status_code=status.HTTP_201_CREATED,
)
async def create_food_category(
    food_category_create_model: FoodCategoryCreateModel,
    food_category_command_service: FoodCategoryCommand = Depends(
        get_food_category_command_service,
    ),
):
    return await food_category_command_service.create_food_category(
        food_category_create_model,
    )


@router.get(
    "/{name}",
    response_model=FoodCategoryReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_food_category(
    name: str,
    food_category_query_service: FoodCategoryQuery = Depends(
        get_food_category_query_service,
    ),
):
    return await food_category_query_service.find_food_category_by_name(name)


@router.get(
    "/{name}/food_items",
    response_model=list[FoodItemReadModel],
    status_code=status.HTTP_200_OK,
)
async def get_food_items_by_category_name(
    name: str,
    food_category_query_service: FoodCategoryQuery = Depends(
        get_food_category_query_service,
    ),
):
    return await food_category_query_service.find_food_items_by_category_name(name)


@router.post(
    "/{name}/food_items",
    response_model=list[FoodItemReadModel],
    status_code=status.HTTP_201_CREATED,
)
async def create_food_items_under_category(
    name: str,
    food_items: list[FoodItemCreateModel],
    food_category_command_service: FoodCategoryCommand = Depends(
        get_food_category_command_service,
    ),
):
    return await food_category_command_service.create_food_items_under_category(
        name,
        food_items,
    )

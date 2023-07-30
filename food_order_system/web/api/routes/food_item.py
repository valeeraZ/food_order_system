from fastapi import APIRouter, Depends, status

from food_order_system.usecase.food_item.food_item_command_model import (
    FoodItemCreateModel,
)
from food_order_system.usecase.food_item.food_item_command_service import (
    FoodItemCommand,
    get_food_item_command_service,
)
from food_order_system.usecase.food_item.food_item_query_model import FoodItemReadModel
from food_order_system.usecase.food_item.food_item_query_service import (
    FoodItemQuery,
    get_food_item_query_service,
)

router = APIRouter(prefix="/food_items", tags=["food items"])


@router.post("/", response_model=FoodItemReadModel, status_code=status.HTTP_201_CREATED)
async def create_food_item(
    food_item_create_model: FoodItemCreateModel,
    food_item_command_service: FoodItemCommand = Depends(get_food_item_command_service),
):
    return await food_item_command_service.create_food_item(food_item_create_model)


@router.get(
    "/{name}",
    response_model=FoodItemReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_food_item(
    name: str,
    food_item_query_service: FoodItemQuery = Depends(get_food_item_query_service),
):
    return await food_item_query_service.find_food_item_by_name(name)

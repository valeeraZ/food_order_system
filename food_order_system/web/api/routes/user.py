from fastapi import APIRouter, Depends, status

from food_order_system.usecase.user.user_command_model import UserCreateModel
from food_order_system.usecase.user.user_command_service import (
    UserCommand,
    get_user_command_service,
)
from food_order_system.usecase.user.user_query_model import UserReadModel
from food_order_system.usecase.user.user_query_service import (
    UserQuery,
    get_user_query_service,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserReadModel, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create_model: UserCreateModel,
    user_command_service: UserCommand = Depends(get_user_command_service),
):
    return await user_command_service.create_user(user_create_model)


@router.get(
    "/{phone_number}",
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    phone_number: str,
    user_query_service: UserQuery = Depends(get_user_query_service),
):
    return await user_query_service.find_user_by_phone_number(phone_number)

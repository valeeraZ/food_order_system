from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from food_order_system.domain.user.user_exception import (
    UserNotCreatedException,
    UserNotFoundException,
)
from food_order_system.infra.db.dependencies import get_db_session
from food_order_system.infra.db.model.user_dto import UserDTO
from food_order_system.infra.db.repository.user import UserRepository
from food_order_system.usecase.user.user_command_model import UserCreateModel
from food_order_system.usecase.user.user_command_service import UserCommand
from food_order_system.usecase.user.user_query_model import UserReadModel
from food_order_system.usecase.user.user_query_service import UserQuery

router = APIRouter(prefix="/users", tags=["users"])


def get_user_query_service(
    session: AsyncSession = Depends(get_db_session),
) -> UserQuery:
    return UserQuery(UserRepository(UserDTO, session))


def get_user_command_service(
    session: AsyncSession = Depends(get_db_session),
) -> UserCommand:
    return UserCommand(UserRepository(UserDTO, session))


@router.post("/", response_model=UserReadModel, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create_model: UserCreateModel,
    user_command_service: UserCommand = Depends(get_user_command_service),
):
    try:
        return await user_command_service.create_user(user_create_model)
    except UserNotCreatedException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@router.get(
    "/{phone_number}",
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    phone_number: str,
    user_query_service: UserQuery = Depends(get_user_query_service),
):
    try:
        return await user_query_service.find_user_by_phone_number(phone_number)
    except UserNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e

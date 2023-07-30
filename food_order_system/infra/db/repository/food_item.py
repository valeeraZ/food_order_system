from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from food_order_system.infra.db.dependencies import get_db_session
from food_order_system.infra.db.model.food_item_dto import FoodItemDTO
from food_order_system.infra.db.repository.base import BaseRepository


class FoodItemRepository(BaseRepository[FoodItemDTO]):
    pass


def get_food_item_repository(
    session: AsyncSession = Depends(get_db_session),
) -> FoodItemRepository:
    return FoodItemRepository(FoodItemDTO, session)

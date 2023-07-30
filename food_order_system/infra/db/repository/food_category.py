from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from food_order_system.infra.db.dependencies import get_db_session
from food_order_system.infra.db.model.food_category_dto import FoodCategoryDTO
from food_order_system.infra.db.repository.base import BaseRepository


class FoodCategoryRepository(BaseRepository[FoodCategoryDTO]):
    pass


def get_food_category_repository(
    session: AsyncSession = Depends(get_db_session),
) -> FoodCategoryRepository:
    return FoodCategoryRepository(FoodCategoryDTO, session)

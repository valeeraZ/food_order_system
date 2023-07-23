from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from food_order_system.infra.db.dependencies import get_db_session

router = APIRouter()


async def is_database_online(session: AsyncSession) -> bool:
    try:
        await session.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


@router.get("/health", status_code=status.HTTP_200_OK, tags=["monitoring"])
async def health_check(
    response: Response,
    session: AsyncSession = Depends(get_db_session),
):
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    if await is_database_online(session):
        response.status_code = status.HTTP_200_OK
        return {"database": "online"}
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return {"database": "offline"}

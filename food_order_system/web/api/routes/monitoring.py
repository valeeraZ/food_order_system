from fastapi import APIRouter, Depends, Response, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from food_order_system.infra.db.dependencies import get_db_session

router = APIRouter()


def is_database_online(session: Session) -> bool:
    try:
        session.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


def is_facebook_online():
    return {"database": "online"}


@router.get("/health", status_code=status.HTTP_200_OK, tags=["monitoring"])
def health_check(response: Response, session: Session = Depends(get_db_session)):
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    if is_database_online(session):
        response.status_code = status.HTTP_200_OK
        return {"database": "online"}
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return {"database": "offline"}

from fastapi.routing import APIRouter

from food_order_system.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)

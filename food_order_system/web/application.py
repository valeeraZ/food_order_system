from importlib import metadata

from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from food_order_system.exception.base_exception_handler import (
    NotCreatedException,
    NotDeletedException,
    NotFoundException,
    NotUpdatedException,
    not_created_exception_handler,
    not_deleted_exception_handler,
    not_found_exception_handler,
    not_updated_exception_handler,
)
from food_order_system.web.api import api_router
from food_order_system.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="food_order_system",
        version=metadata.version("food_order_system"),
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    # add exception handlers
    app.add_exception_handler(NotFoundException, not_found_exception_handler)
    app.add_exception_handler(NotCreatedException, not_created_exception_handler)
    app.add_exception_handler(NotUpdatedException, not_updated_exception_handler)
    app.add_exception_handler(NotDeletedException, not_deleted_exception_handler)

    return app

from fastapi import Request
from fastapi.responses import JSONResponse

from food_order_system.exception.base_exception import (
    NotCreatedException,
    NotDeletedException,
    NotFoundException,
    NotUpdatedException,
)


async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content=str(exc),
    )


async def not_created_exception_handler(request: Request, exc: NotCreatedException):
    return JSONResponse(
        status_code=400,
        content=str(exc),
    )


async def not_updated_exception_handler(request: Request, exc: NotUpdatedException):
    return JSONResponse(
        status_code=400,
        content=str(exc),
    )


async def not_deleted_exception_handler(request: Request, exc: NotDeletedException):
    return JSONResponse(
        status_code=400,
        content=str(exc),
    )

from dataclasses import dataclass
from typing import Callable, Dict, Type

import logging

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette import status

logger = logging.getLogger(__name__)


class StacApiError(Exception):
    pass


class ConflictError(StacApiError):
    pass


class NotFoundError(StacApiError):
    pass


class ForeignKeyError(StacApiError):
    pass


class DatabaseError(StacApiError):
    pass


DEFAULT_STATUS_CODES = {
    NotFoundError: status.HTTP_404_NOT_FOUND,
    ConflictError: status.HTTP_409_CONFLICT,
    ForeignKeyError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    DatabaseError: status.HTTP_424_FAILED_DEPENDENCY,
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
}


def exception_handler_factory(status_code: int) -> Callable:
    """
    Create a FastAPI exception handler from a status code.
    """

    def handler(request: Request, exc: Exception):
        logger.error(exc, exc_info=True)
        return JSONResponse(content={"detail": str(exc)}, status_code=status_code)

    return handler


def add_exception_handlers(
    app: FastAPI, status_codes: Dict[Type[Exception], int]
) -> None:
    """
    Add exception handlers to the FastAPI app.
    """
    for (exc, code) in status_codes.items():
        app.add_exception_handler(exc, exception_handler_factory(code))

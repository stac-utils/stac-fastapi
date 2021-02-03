"""Error handling"""

import logging
from typing import Callable, Dict, Type

from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)


class StacApiError(Exception):
    """Generic API error"""

    pass


class ConflictError(StacApiError):
    """Database conflict"""

    pass


class NotFoundError(StacApiError):
    """Resource not found"""

    pass


class ForeignKeyError(StacApiError):
    """Foreign key error (collection does not exist)"""

    pass


class DatabaseError(StacApiError):
    """Generic database errors"""

    pass


DEFAULT_STATUS_CODES = {
    NotFoundError: status.HTTP_404_NOT_FOUND,
    ConflictError: status.HTTP_409_CONFLICT,
    ForeignKeyError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    DatabaseError: status.HTTP_424_FAILED_DEPENDENCY,
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
}


def exception_handler_factory(status_code: int) -> Callable:
    """Create a FastAPI exception handler for a particular status code.

    Args:
        status_code: HTTP status code.

    Returns:
        callable: an exception handler.
    """

    def handler(request: Request, exc: Exception):
        """i handle exceptions!!"""
        logger.error(exc, exc_info=True)
        return JSONResponse(content={"detail": str(exc)}, status_code=status_code)

    return handler


def add_exception_handlers(
    app: FastAPI, status_codes: Dict[Type[Exception], int]
) -> None:
    """Add exception handlers to the FastAPI application.

    Args:
        app: the FastAPI application.
        status_codes: mapping between exceptions and status codes.

    Returns:
        None
    """
    # """
    # Add exception handlers to the FastAPI app.
    # """
    for (exc, code) in status_codes.items():
        app.add_exception_handler(exc, exception_handler_factory(code))

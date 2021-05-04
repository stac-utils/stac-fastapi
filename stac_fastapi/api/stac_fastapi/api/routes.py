"""route factories."""
import inspect
import logging
from typing import Callable, Type, Union

from fastapi import Depends
from pydantic import BaseModel
from starlette.requests import Request

from stac_fastapi.api.models import APIRequest

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)


def create_endpoint(
    func: Callable, request_model: Union[Type[APIRequest], Type[BaseModel]]
) -> Callable:
    """
    Create a FastAPI endpoint.

    This endpoint executes code in an external threadpool which is then awaited by the event loop.
    https://fastapi.tiangolo.com/async/#path-operation-functions

    Accepts either an `stac_fastapi.api.models.APIRequest` or `pydantic.BaseModel`.

    Pydantic models are good for validating request bodies (ex. POST requests), and expect the signature of the
    callable matches that of the request model.

    APIRequest is good for validating query/path parameters (ex. GET requests) and allows for FastAPI dependency
    injection.  It is expected the that the return of `APIRequest.kwargs` matches that of the callable.

    Args:
        func: the wrapped function.
        request_model: either `stac_fastapi.api.models.APIRequest` or `pydantic.BaseModel`.

    Returns:
        callable: fastapi route which may be added to a router/application
    """
    if not inspect.iscoroutinefunction(func):
        if issubclass(request_model, APIRequest):

            def _endpoint(
                request: Request,
                request_data: request_model = Depends(),  # type:ignore
            ):
                """Endpoint."""
                resp = func(
                    request=request, **request_data.kwargs()  # type:ignore
                )
                return resp

        else:

            def _endpoint(
                request: Request,
                request_data: request_model,  # type:ignore
            ):
                """Endpoint."""
                resp = func(request_data, request=request)
                return resp

        return _endpoint
    else:
        if issubclass(request_model, APIRequest):

            async def _endpoint(
                request: Request,
                request_data: request_model = Depends(),  # type:ignore
            ):
                """Endpoint."""
                resp = await func(
                    request=request, **request_data.kwargs()  # type:ignore
                )
                return resp

        else:

            async def _endpoint(
                request: Request,
                request_data: request_model,  # type:ignore
            ):
                """Endpoint."""
                resp = await func(request_data, request=request)
                return resp

        return _endpoint

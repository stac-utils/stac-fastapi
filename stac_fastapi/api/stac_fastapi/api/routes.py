"""route factories."""
from typing import Any, Callable, Dict, Type, Union

from fastapi import Depends
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.models import APIRequest


def _wrap_response(resp: Any, response_class: Type[Response]) -> Response:
    if isinstance(resp, Response):
        return resp
    else:
        return response_class(resp)


def create_async_endpoint(
    func: Callable,
    request_model: Union[Type[APIRequest], Type[BaseModel], Dict],
    response_class: Type[Response] = JSONResponse,
):
    """Wrap a coroutine in another coroutine which may be used to create a FastAPI endpoint."""
    if issubclass(request_model, APIRequest):

        async def _endpoint(
            request: Request,
            request_data: request_model = Depends(),  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(
                await func(request=request, **request_data.kwargs()), response_class
            )

    elif issubclass(request_model, BaseModel):

        async def _endpoint(
            request: Request,
            request_data: request_model,  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(
                await func(request_data, request=request), response_class
            )

    else:

        async def _endpoint(
            request: Request,
            request_data: Dict[str, Any],  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(
                await func(request_data, request=request), response_class
            )

    return _endpoint


def create_sync_endpoint(
    func: Callable,
    request_model: Union[Type[APIRequest], Type[BaseModel], Dict],
    response_class: Type[Response] = JSONResponse,
):
    """Wrap a function in another function which may be used to create a FastAPI endpoint."""
    if issubclass(request_model, APIRequest):

        def _endpoint(
            request: Request,
            request_data: request_model = Depends(),  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(
                func(request=request, **request_data.kwargs()), response_class
            )

    elif issubclass(request_model, BaseModel):

        def _endpoint(
            request: Request,
            request_data: request_model,  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(func(request_data, request=request), response_class)

    else:

        def _endpoint(
            request: Request,
            request_data: Dict[str, Any],  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(func(request_data, request=request), response_class)

    return _endpoint

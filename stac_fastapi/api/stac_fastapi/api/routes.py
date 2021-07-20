"""route factories."""
from typing import Any, Callable, Dict, Type, Union

from fastapi import Depends
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from stac_fastapi.api.models import APIRequest


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
            resp = await func(
                request=request, **request_data.kwargs()  # type:ignore
            )
            return response_class(resp)

    elif issubclass(request_model, BaseModel):

        async def _endpoint(
            request: Request,
            request_data: request_model,  # type:ignore
        ):
            """Endpoint."""
            resp = await func(request_data, request=request)
            return response_class(resp)

    else:

        async def _endpoint(
            request: Request,
            request_data: Dict[str, Any],  # type:ignore
        ):
            """Endpoint."""
            resp = await func(request_data, request=request)
            return response_class(resp)

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
            resp = func(
                request=request, **request_data.kwargs()  # type:ignore
            )
            return response_class(resp)

    elif issubclass(request_model, BaseModel):

        def _endpoint(
            request: Request,
            request_data: request_model,  # type:ignore
        ):
            """Endpoint."""
            resp = func(request_data, request=request)
            return response_class(resp)

    else:

        def _endpoint(
            request: Request,
            request_data: Dict[str, Any],  # type:ignore
        ):
            """Endpoint."""
            resp = func(request_data, request=request)
            return response_class(resp)

    return _endpoint

"""route factories."""
from typing import Callable, Type

from fastapi import Depends
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

from stac_fastapi.api.models import APIRequest


def response_class():
    """Use OrJSON if possible for serialization performance, falling back on starlette's implementation of JSON"""
    try:
        import orjson

        class OrjsonResponse(JSONResponse):
            def render(self, content: Any) -> bytes:
                return orjson.dumps(content)

        return OrjsonResponse
    except ImportError:
        return JSONResponse


# TODO: Only use one endpoint factory
def create_endpoint_from_model(
    func: Callable, request_model: Type[BaseModel]
) -> Callable:
    """Create a FastAPI endpoint from pydantic model.

    Wrap a callable in a function which uses the desired request model.  It is expected
    that the signature of the callable matches that of the request model.  This is best for validating
    request bodies (ex. POST requests).

    Args:
        func: the wrapped function.
        request_model: a pydantic model.

    Returns:
        callable: fastapi route which may be added to a router/application
    """

    def _endpoint(
        request: Request,
        request_data: request_model,  # type:ignore
    ):
        """Endpoint."""
        resp = func(request_data, request=request)
        return response_class()(resp.dict(by_alias=True, exclude_none=True))

    return _endpoint


def create_endpoint_with_depends(
    func: Callable,
    request_model: Type[APIRequest],
) -> Callable:
    """Create a FastAPI endpoint from an `APIRequest` (dataclass).

    Wrap a callable in a function which uses the desired `APIRequest` to define request parameters.  It is expected
    that the return of `APIRequest.kwargs` matches that of the callable.  This works best for validating query/path
    parameters (ex. GET request) and allows for dependency injection.

    Args:
        func: the wrapped function
        request_model: subclass of `APIRequest`

    Returns:
        callable: fastapi route which may be added to a router/application
    """

    def _endpoint(
        request: Request,
        request_data: request_model = Depends(),  # type:ignore
    ):
        """Endpoint."""
        resp = func(
            request=request, **request_data.kwargs()  # type:ignore
        )
        return response_class()(resp.dict(by_alias=True, exclude_none=True))

    return _endpoint

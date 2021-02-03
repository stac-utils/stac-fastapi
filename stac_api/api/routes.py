"""route factories"""
from typing import Callable, Type

from fastapi import Depends
from pydantic import BaseModel
from starlette.requests import Request

from stac_api.api.models import APIRequest


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
        """endpoint"""
        resp = func(request_data, request=request)
        return resp

    return _endpoint


def create_endpoint_with_depends(
    func: Callable,
    request_model: Type[APIRequest],
) -> Callable:
    # """
    # Create a fastapi endpoint where request model is a dataclass.  This works best for validating query/patm params.
    # """
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
        """endpoint"""
        resp = func(
            request=request, **request_data.kwargs()  # type:ignore
        )
        return resp

    return _endpoint

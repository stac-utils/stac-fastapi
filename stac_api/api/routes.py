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
    """
    Create a FastAPI endpoint where request model is a pydantic model.  This works best for validating request bodies
    (POST/PUT etc.)
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
    """
    Create a fastapi endpoint where request model is a dataclass.  This works best for validating query/patm params.
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

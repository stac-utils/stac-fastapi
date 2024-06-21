"""Route factories."""

import copy
import functools
import inspect
import warnings
from typing import Any, Callable, Dict, List, Optional, Type, TypedDict, Union

from fastapi import Depends, params
from fastapi.dependencies.utils import get_parameterless_sub_dependant
from pydantic import BaseModel
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import BaseRoute, Match
from starlette.status import HTTP_204_NO_CONTENT

from stac_fastapi.api.models import APIRequest


def _wrap_response(resp: Any) -> Any:
    if resp is not None:
        return resp
    else:  # None is returned as 204 No Content
        return Response(status_code=HTTP_204_NO_CONTENT)


def sync_to_async(func):
    """Run synchronous function asynchronously in a background thread."""

    @functools.wraps(func)
    async def run(*args, **kwargs):
        return await run_in_threadpool(func, *args, **kwargs)

    return run


def create_async_endpoint(
    func: Callable,
    request_model: Union[Type[APIRequest], Type[BaseModel], Dict],
    response_class: Optional[Type[Response]] = None,
):
    """Wrap a function in a coroutine which may be used to create a FastAPI endpoint.

    Synchronous functions are executed asynchronously using a background thread.
    """

    if response_class:
        warnings.warn(
            "`response_class` option is deprecated, please set the Response class directly in the endpoint.",  # noqa: E501
            DeprecationWarning,
        )

    if not inspect.iscoroutinefunction(func):
        func = sync_to_async(func)

    if issubclass(request_model, APIRequest):

        async def _endpoint(
            request: Request,
            request_data: request_model = Depends(),  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(await func(request=request, **request_data.kwargs()))

    elif issubclass(request_model, BaseModel):

        async def _endpoint(
            request: Request,
            request_data: request_model,  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(await func(request_data, request=request))

    else:

        async def _endpoint(
            request: Request,
            request_data: Dict[str, Any],  # type:ignore
        ):
            """Endpoint."""
            return _wrap_response(await func(request_data, request=request))

    return _endpoint


class Scope(TypedDict, total=False):
    """More strict version of Starlette's Scope."""

    # https://github.com/encode/starlette/blob/6af5c515e0a896cbf3f86ee043b88f6c24200bcf/starlette/types.py#L3
    path: str
    method: str
    type: Optional[str]


def add_route_dependencies(
    routes: List[BaseRoute], scopes: List[Scope], dependencies=List[params.Depends]
) -> None:
    """Add dependencies to routes.

    Allows a developer to add dependencies to a route after the route has been
    defined.

    "*" can be used for path or method to match all allowed routes.

    Returns:
        None
    """
    for scope in scopes:
        _scope = copy.deepcopy(scope)
        for route in routes:
            if scope["path"] == "*":
                _scope["path"] = route.path

            if scope["method"] == "*":
                _scope["method"] = list(route.methods)[0]

            match, _ = route.matches({"type": "http", **_scope})
            if match != Match.FULL:
                continue

            # Ignore paths without dependants, e.g. /api, /api.html, /docs/oauth2-redirect
            if not hasattr(route, "dependant"):
                continue

            # Mimicking how APIRoute handles dependencies:
            # https://github.com/tiangolo/fastapi/blob/1760da0efa55585c19835d81afa8ca386036c325/fastapi/routing.py#L408-L412
            for depends in dependencies[::-1]:
                route.dependant.dependencies.insert(
                    0,
                    get_parameterless_sub_dependant(
                        depends=depends, path=route.path_format
                    ),
                )

            # Register dependencies directly on route so that they aren't ignored if
            # the routes are later associated with an app (e.g.
            # app.include_router(router))
            # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/applications.py#L337-L360
            # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/routing.py#L677-L678
            route.dependencies.extend(dependencies)

"""Route factories."""

import copy
import functools
import inspect
from typing import Any, Awaitable, Callable, Dict, List, Optional, Type, TypedDict, Union

from fastapi import Depends, FastAPI, params
from fastapi.datastructures import DefaultPlaceholder
from fastapi.dependencies.utils import get_dependant, get_parameterless_sub_dependant
from fastapi.routing import APIRoute, request_response
from pydantic import BaseModel
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import BaseRoute, Match
from starlette.status import HTTP_204_NO_CONTENT

from stac_fastapi.types.search import APIRequest


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
) -> Callable[[Any, Any], Awaitable[Any]]:
    """Wrap a function in a coroutine which may be used to create a FastAPI endpoint.

    Synchronous functions are executed asynchronously using a background thread.
    """

    if not inspect.iscoroutinefunction(func):
        func = sync_to_async(func)

    _endpoint: Callable[[Any, Any], Awaitable[Any]]

    if isinstance(request_model, dict):

        async def _endpoint(request: Request, request_data: Dict[str, Any]):
            """Endpoint."""
            return _wrap_response(await func(request_data, request=request))

    elif issubclass(request_model, APIRequest):

        async def _endpoint(request: Request, request_data=Depends(request_model)):  # type: ignore
            """Endpoint."""
            return _wrap_response(await func(request=request, **request_data.kwargs()))

    elif issubclass(request_model, BaseModel):

        async def _endpoint(request: Request, request_data: request_model):  # type: ignore
            """Endpoint."""
            return _wrap_response(await func(request_data, request=request))

    else:
        raise ValueError(f"Unsupported type for request model {type(request_model)}")

    return _endpoint


class Scope(TypedDict, total=False):
    """More strict version of Starlette's Scope."""

    # https://github.com/encode/starlette/blob/6af5c515e0a896cbf3f86ee043b88f6c24200bcf/starlette/types.py#L3
    path: str
    method: str
    type: Optional[str]


def add_route_dependencies(
    routes: List[BaseRoute], scopes: List[Scope], dependencies: List[params.Depends]
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
                # NOTE: ignore type, because BaseRoute has no "path" attribute
                # but APIRoute does.
                _scope["path"] = route.path  # type: ignore

            # NOTE: ignore type, because BaseRoute has no "method" attribute
            # but APIRoute does.
            if scope["method"] == "*":
                _scope["method"] = list(route.methods)[0]  # type: ignore

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
                        # NOTE: ignore type, because BaseRoute has no "path_format"
                        # attribute but APIRoute does.
                        depends=depends,
                        path=route.path_format,  # type: ignore
                    ),
                )

            # Register dependencies directly on route so that they aren't ignored if
            # the routes are later associated with an app (e.g.
            # app.include_router(router))
            # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/applications.py#L337-L360
            # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/routing.py#L677-L678
            # NOTE: ignore type, because BaseRoute has no "dependencies" attribute
            # but APIRoute does.
            route.dependencies.extend(dependencies)  # type: ignore


def add_direct_response(app: FastAPI) -> None:
    """
    Setup FastAPI application's endpoints to return Response Object directly, avoiding
    Pydantic validation and FastAPI (slow) serialization.

    ref: https://gist.github.com/Zaczero/00f3a2679ebc0a25eb938ed82bc63553
    """

    def wrap_endpoint(endpoint: Callable, cls: Type[Response]):
        @functools.wraps(endpoint)
        async def wrapper(*args, **kwargs):
            content = await endpoint(*args, **kwargs)
            return content if isinstance(content, Response) else cls(content)

        return wrapper

    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue

        response_class = route.response_class
        if isinstance(response_class, DefaultPlaceholder):
            response_class = response_class.value

        if issubclass(response_class, Response):
            route.endpoint = wrap_endpoint(route.endpoint, response_class)
            route.dependant = get_dependant(path=route.path_format, call=route.endpoint)
            route.app = request_response(route.get_route_handler())

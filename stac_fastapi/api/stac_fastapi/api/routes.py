"""Route factories."""

import copy
import functools
import inspect
from collections import defaultdict
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypedDict, Union

from fastapi import Depends, HTTPException, params, status
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
):
    """Wrap a function in a coroutine which may be used to create a FastAPI endpoint.

    Synchronous functions are executed asynchronously using a background thread.
    """

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


def merge_dependencies1(*dependencies: Callable) -> Callable:
    """
    This function wraps the given callables (dependencies) and
    wraps them in FastAPIs Depends. It returns a function
    containing these dependencies in its signature.

    :param dependencies: The dependencies to wrap
    :return: A callable which returns a list of the results of
    the dependencies
    """

    def merged_dependencies(**kwargs):
        result = next((item for item in kwargs.values() if item is not None), None)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )
        return result

    merged_dependencies.__signature__ = inspect.Signature(  # type: ignore
        parameters=[
            inspect.Parameter(f"dep{key}", inspect.Parameter.KEYWORD_ONLY, default=dep)
            for key, dep in enumerate(dependencies)
        ]
    )
    return merged_dependencies


def merge_dependencies2(*dependencies: Callable) -> Callable:
    """
    This function wraps the given callables (dependencies) and
    wraps them in FastAPIs Depends. It returns a function
    containing these dependencies in its signature.

    :param dependencies: The dependencies to wrap
    :return: A callable which returns the first non none result of
    the dependencies
    """

    async def merged_dependencies(**kwargs):
        for dep_key, dep in dependencies_key.items():
            dep_kwargs = {
                kwarg_key.removeprefix(dep_key): kwarg_value
                for kwarg_key, kwarg_value in kwargs.items()
                if kwarg_key.startswith(dep_key)
            }

            try:
                result = await dep.dependency(**dep_kwargs)

                if result:
                    return result

            except HTTPException as e:
                if e.status_code != 401:
                    raise e

                continue

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    dependencies_key = {}
    sub_dependencies = []
    for key, dep in enumerate(dependencies):
        dependencies_key[f"dep{key}_"] = dep

        if isinstance(dep, params.Depends):
            for sub_key, parameter in inspect.signature(
                dep.dependency
            ).parameters.items():
                dummy_parameter = parameter.replace(name=f"dep{key}_{sub_key}")
                sub_dependencies.append(dummy_parameter)

    merged_dependencies.__signature__ = inspect.Signature(  # type: ignore
        parameters=sub_dependencies
    )
    return merged_dependencies


def map_route_securities(
    route_securites: List[Tuple[List[Scope], List[Depends]]],
) -> Dict:
    """Map route securities.

    Allows a developer to add dependencies to a route after the route has been
    defined.

    "*" can be used for path or method to match all allowed routes.

    Returns:
        None
    """
    mapped_scopes = defaultdict(list)

    for scopes, securities in route_securites:
        for scope in scopes:
            for method in scope["method"]:
                mapped_scopes[scope["path"]][method].append(securities)

    return mapped_scopes


def add_route_securities(
    routes: List[BaseRoute], route_securites: List[Tuple[List[Scope], List[Depends]]]
) -> None:
    """Add securities to routes.

    Allows a developer to add securities to a route after the route has been
    defined.

    "*" can be used for path or method to match all allowed routes or methods.

    Returns:
        None
    """
    mapped_scopes = map_route_securities(route_securites=route_securites)

    default_scope = mapped_scopes.pop("*", {})

    for route in routes:
        if not hasattr(route, "dependant"):
            continue

        scope = mapped_scopes.get(route.path, defaultdict(list))
        route_securities = []

        for default_method, default_security in default_scope.items():
            scope[default_method].append(default_security)

        for method, security in scope.items():
            method = scope["method"]
            if method == "*":
                method = list(route.methods)[0]

            match, _ = route.matches(
                {"type": "http", **{"routes": [route.path], "method": [method]}}
            )
            if match:
                route_securities.append(security)

        route_security = (
            Depends(merge_dependencies2(*route_securities))
            if len(route_securities) > 1
            else route_securities[0]
        )

        # route_security = Depends(merge_dependencies1(*route_securities))

        # Mimicking how APIRoute handles dependencies:
        # https://github.com/tiangolo/fastapi/blob/1760da0efa55585c19835d81afa8ca386036c325/fastapi/routing.py#L408-L412
        route.dependant.dependencies.insert(
            0,
            get_parameterless_sub_dependant(
                depends=route_security, path=route.path_format
            ),
        )

        # Register dependencies directly on route so that they aren't ignored if
        # the routes are later associated with an app (e.g.
        # app.include_router(router))
        # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/applications.py#L337-L360
        # https://github.com/tiangolo/fastapi/blob/58ab733f19846b4875c5b79bfb1f4d1cb7f4823f/fastapi/routing.py#L677-L678
        route.dependencies.extend(route_securities)


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

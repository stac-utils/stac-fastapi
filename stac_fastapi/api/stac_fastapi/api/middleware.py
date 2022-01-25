"""api middleware."""

from json import loads
from logging import getLogger
from os import environ, path
from typing import Any, Callable, Dict, Final, List, Optional

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.routing import Match

logger: Final = getLogger(__file__)


def router_middleware(app: FastAPI, router: APIRouter):
    """Add middleware to a specific router, assumes no router prefix."""

    def deco(func: Callable) -> Callable:
        async def _middleware(request: Request, call_next):
            # Check if scopes match
            matches = any(
                [
                    route.matches(request.scope)[0] == Match.FULL
                    for route in router.routes
                ]
            )
            if matches:  # Run the middleware if they do
                return await func(request, call_next)
            else:  # Otherwise skip the middleware
                return await call_next(request)

        app.add_middleware(BaseHTTPMiddleware, dispatch=_middleware)
        return func

    return deco


class MiddlewareConfig:
    """Represents a middleware class plus any configuration detail."""

    def __init__(self, middleware: Any, config: Optional[Dict[str, Any]] = None):
        """Defaults config to empty dictionary if not provided."""
        self.middleware = middleware
        self.config = {} if config is None else config


def append_runtime_middlewares(
    middlewares: List[MiddlewareConfig],
) -> List[MiddlewareConfig]:
    """Add any middlewares specified via environment variable and configure if appropriate."""
    extended_middlewares = middlewares.copy()
    has_cors_middleware = (
        len(
            [
                entry
                for entry in middlewares
                if isinstance(entry.middleware, CORSMiddleware)
            ]
        )
        > 0
    )
    if not has_cors_middleware:
        cors_config_location_key: Final = "CORS_CONFIG_LOCATION"
        if cors_config_location_key in environ:
            cors_config_path = environ[cors_config_location_key]
            logger.info(f"looking for CORS config file at {cors_config_path}")
            if path.exists(cors_config_path):
                try:
                    with open(cors_config_path, "r") as cors_config_file:
                        cors_config = loads("".join(cors_config_file.readlines()))
                        extended_middlewares.append(
                            MiddlewareConfig(CORSMiddleware, cors_config)
                        )
                        logger.debug(f"loaded CORS config {cors_config}")
                except ValueError as e:
                    logger.error(f"error parsing JSON at {cors_config_path}: {e}")
                except OSError as e:
                    logger.error(f"error reading {cors_config_path}: {e}")
            else:
                logger.warning(f"CORS config not found at {cors_config_path}")

    return extended_middlewares

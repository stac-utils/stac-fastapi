"""api middleware."""

from logging import getLogger
from typing import Callable, Final, Optional, Sequence

from fastapi import APIRouter, FastAPI
from fastapi.middleware import cors
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.routing import Match
from starlette.types import ASGIApp

from stac_fastapi.api.config import env_to_bool, env_to_int, env_to_sequence, env_to_str

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


class CORSMiddleware(cors.CORSMiddleware):
    """Starlette CORS Middleware with default."""

    def __init__(
        self,
        app: ASGIApp,
        allow_origins: Optional[Sequence[str]] = None,
        allow_methods: Optional[Sequence[str]] = None,
        allow_headers: Optional[Sequence[str]] = None,
        allow_credentials: Optional[bool] = None,
        allow_origin_regex: Optional[str] = None,
        expose_headers: Optional[Sequence[str]] = None,
        max_age: Optional[int] = None,
    ) -> None:
        """Create CORSMiddleware Object."""
        allow_origins = (
            env_to_sequence("CORS_ALLOW_ORIGINS", ("*",))
            if allow_origins is None
            else allow_origins
        )
        allow_methods = (
            env_to_sequence("CORS_ALLOW_METHODS", ("*",))
            if allow_methods is None
            else allow_methods
        )
        allow_headers = (
            env_to_sequence("CORS_ALLOW_HEADERS", ("*",))
            if allow_headers is None
            else allow_headers
        )
        allow_credentials = (
            env_to_bool("CORS_ALLOW_CREDENTIALS", False)
            if allow_credentials is None
            else allow_credentials
        )
        allow_origin_regex = (
            env_to_str("CORS_ALLOW_ORIGIN_REGEX", None)
            if allow_origin_regex is None
            else allow_origin_regex
        )
        if allow_origin_regex is not None:
            logger.info(
                "CORS_ALLOW_ORIGIN_REGEX present and will override CORS_ALLOW_ORIGINS"
            )
            allow_origins = ""
        expose_headers = (
            env_to_sequence("CORS_EXPOSE_HEADERS", ("*",))
            if expose_headers is None
            else expose_headers
        )
        max_age = env_to_int("CORS_MAX_AGE", 600) if max_age is None else max_age
        logger.debug(
            f"""
            CORS configuration
            allow_origins: {allow_origins}
            allow_methods: {allow_methods}
            allow_headers: {allow_headers}
            allow_credentials: {allow_credentials}
            allow_origin_regex: {allow_origin_regex}
            expose_headers: {expose_headers}
            max_age: {max_age}
        """
        )
        super().__init__(
            app,
            allow_origins=allow_origins,
            allow_methods=allow_methods,
            allow_headers=allow_headers,
            allow_credentials=allow_credentials,
            allow_origin_regex=allow_origin_regex,
            expose_headers=expose_headers,
            max_age=max_age,
        )

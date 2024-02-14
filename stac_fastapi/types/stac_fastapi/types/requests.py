"""Requests helpers."""

import os

from starlette.requests import Request


def get_base_url(request: Request) -> str:
    """Get base URL with respect of APIRouter prefix."""
    if base_url := os.environ.get("REQUEST_BASE_URL"):
        return base_url

    app = request.app
    if not app.state.router_prefix:
        return str(request.base_url)
    else:
        return "{}{}/".format(
            str(request.base_url), app.state.router_prefix.lstrip("/")
        )

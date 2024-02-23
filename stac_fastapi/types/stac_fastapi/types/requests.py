"""Requests helpers."""

from starlette.requests import Request


def get_base_url(request: Request) -> str:
    """Get base URL with respect of APIRouter prefix."""
    app = request.app
    if not app.state.router_prefix:
        return str(request.base_url)
    else:
        return "{}{}/".format(str(request.base_url), app.state.router_prefix.lstrip("/"))

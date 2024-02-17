"""Requests helpers."""

from starlette.requests import Request


def get_base_url(request: Request) -> str:
    """Get base URL with respect of APIRouter prefix."""
    app = request.app
    base_url = str(request.base_url)
    if url := app.state.settings.base_url:
        base_url = url
    if not app.state.router_prefix:
        return base_url
    else:
        return "{}{}/".format(base_url, app.state.router_prefix.lstrip("/"))

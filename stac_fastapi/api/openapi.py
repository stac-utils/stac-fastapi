"""openapi."""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.requests import Request
from starlette.responses import JSONResponse

from stac_fastapi.api.config import ApiExtensions
from stac_fastapi.types.config import ApiSettings


class VndOaiResponse(JSONResponse):
    """JSON with custom, vendor content-type."""

    media_type = "application/vnd.oai.openapi+json;version=3.0"


def update_openapi(app: FastAPI) -> FastAPI:
    """Update OpenAPI response content-type.

    This function modifies the openapi route to comply with the STAC API spec's
    required content-type response header
    """
    urls = (server_data.get("url") for server_data in app.servers)
    server_urls = {url for url in urls if url}

    async def openapi(req: Request) -> JSONResponse:
        root_path = req.scope.get("root_path", "").rstrip("/")
        if root_path not in server_urls:
            if root_path and app.root_path_in_servers:
                app.servers.insert(0, {"url": root_path})
                server_urls.add(root_path)
        return VndOaiResponse(app.openapi())

    # Remove the default openapi route
    app.router.routes = list(
        filter(lambda r: r.path != app.openapi_url, app.router.routes)
    )
    # Add the updated openapi route
    app.add_route(app.openapi_url, openapi, include_in_schema=False)
    return app


# TODO: Remove or fix, this is currently unused
# and calls a missing method on ApiSettings
def config_openapi(app: FastAPI, settings: ApiSettings):
    """Config openapi."""

    def custom_openapi():
        """Config openapi."""
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title="Arturo STAC API", version="0.1", routes=app.routes
        )

        if settings.api_extension_is_enabled(ApiExtensions.fields):
            openapi_schema["paths"]["/search"]["get"]["responses"]["200"]["content"][
                "application/json"
            ]["schema"] = {"$ref": "#/components/schemas/ItemCollection"}
            openapi_schema["paths"]["/search"]["post"]["responses"]["200"]["content"][
                "application/json"
            ]["schema"] = {"$ref": "#/components/schemas/ItemCollection"}

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi

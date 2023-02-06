"""openapi."""
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route, request_response


def update_openapi(app: FastAPI) -> FastAPI:
    """Update OpenAPI response content-type.

    This function modifies the openapi route to comply with the STAC API spec's
    required content-type response header.
    """
    # Find the route for the openapi_url in the app.
    openapi_route: Route = next(
        route for route in app.router.routes if route.path == app.openapi_url
    )

    # Create a patched endpoint that modifies the content type of the response
    async def patched_openapi_endpoint(req: Request) -> Response:
        # Get the response from the original endpoint
        response: JSONResponse = await openapi_route.endpoint(req)
        # Update the content type header in place
        response.headers[
            "content-type"
        ] = "application/vnd.oai.openapi+json;version=3.0"
        # Return the updated response
        return response

    # When a route is accessed the `handle` function will call `self.app`. So we can
    # leave the `endpoint` the original function for use in the patched function and
    # just update the `app` to use the patched function.
    openapi_route.app = request_response(patched_openapi_endpoint)

    # return the patched app
    return app

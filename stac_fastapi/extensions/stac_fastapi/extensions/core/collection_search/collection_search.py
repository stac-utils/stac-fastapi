"""Collection-Search extension."""

from enum import Enum
from typing import List, Optional, Union

import attr
from fastapi import APIRouter, FastAPI
from stac_pydantic.api.collections import Collections
from stac_pydantic.shared import MimeTypes

from stac_fastapi.api.models import GeoJSONResponse, create_request_model
from stac_fastapi.api.routes import create_async_endpoint
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.extension import ApiExtension

from .client import AsyncBaseCollectionSearchClient, BaseCollectionSearchClient
from .request import BaseCollectionSearchGetRequest, BaseCollectionSearchPostRequest


class CollectionSearchConformanceClasses(str, Enum):
    """Conformance classes for the Collection-Search extension.

    See
    https://github.com/stac-api-extensions/collection-search
    """

    COLLECTIONSEARCH = "https://api.stacspec.org/v1.0.0-rc.1/collection-search"
    BASIS = "http://www.opengis.net/spec/ogcapi-common-2/1.0/conf/simple-query"


@attr.s
class CollectionSearchExtension(ApiExtension):
    """Collection-Search Extension.

    The Collection-Search extension adds functionality to the `GET - /collections`
    endpoint which allows the caller to include or exclude specific from the API
    response.
    Registering this extension with the application has the added effect of
    removing the `ItemCollection` response model from the `/search` endpoint, as
    the Fields extension allows the API to return potentially invalid responses
    by excluding fields which are required by the STAC spec, such as geometry.

    https://github.com/stac-api-extensions/collection-search

    Attributes:
        conformance_classes (list): Defines the list of conformance classes for
            the extension
    """

    GET: BaseCollectionSearchGetRequest = attr.ib(default=BaseCollectionSearchGetRequest)
    POST = None

    conformance_classes: List[str] = attr.ib(
        default=[
            CollectionSearchConformanceClasses.COLLECTIONSEARCH,
            CollectionSearchConformanceClasses.BASIS,
        ]
    )
    schema_href: Optional[str] = attr.ib(default=None)

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app (fastapi.FastAPI): target FastAPI application.

        Returns:
            None
        """
        pass

    @classmethod
    def from_extensions(
        cls,
        extensions: List[ApiExtension],
        schema_href: Optional[str] = None,
    ) -> "CollectionSearchExtension":
        """Create CollectionSearchExtension object from extensions."""

        conformance_classes = [
            CollectionSearchConformanceClasses.COLLECTIONSEARCH,
            CollectionSearchConformanceClasses.BASIS,
        ]
        for ext in extensions:
            conformance_classes.extend(ext.conformance_classes)

        get_request_model = create_request_model(
            model_name="CollectionsGetRequest",
            base_model=BaseCollectionSearchGetRequest,
            extensions=extensions,
            request_type="GET",
        )

        return cls(
            GET=get_request_model,
            conformance_classes=conformance_classes,
            schema_href=schema_href,
        )


@attr.s
class CollectionSearchPostExtension(CollectionSearchExtension):
    """Collection-Search Extension.

    Extents the collection-search extension with an additional
    POST - /collections endpoint

    NOTE: the POST - /collections endpoint can be conflicting with the
    POST /collections endpoint registered for the Transaction extension.

    https://github.com/stac-api-extensions/collection-search

    Attributes:
        conformance_classes (list): Defines the list of conformance classes for
            the extension
    """

    client: Union[AsyncBaseCollectionSearchClient, BaseCollectionSearchClient] = attr.ib()
    settings: ApiSettings = attr.ib()
    conformance_classes: List[str] = attr.ib(
        default=[
            CollectionSearchConformanceClasses.COLLECTIONSEARCH,
            CollectionSearchConformanceClasses.BASIS,
        ]
    )
    schema_href: Optional[str] = attr.ib(default=None)
    router: APIRouter = attr.ib(factory=APIRouter)

    GET: BaseCollectionSearchGetRequest = attr.ib(default=BaseCollectionSearchGetRequest)
    POST: BaseCollectionSearchPostRequest = attr.ib(
        default=BaseCollectionSearchPostRequest
    )

    def register(self, app: FastAPI) -> None:
        """Register the extension with a FastAPI application.

        Args:
            app: target FastAPI application.

        Returns:
            None
        """
        self.router.prefix = app.state.router_prefix

        self.router.add_api_route(
            name="Collections",
            path="/collections",
            methods=["POST"],
            response_model=(
                Collections if self.settings.enable_response_models else None
            ),
            responses={
                200: {
                    "content": {
                        MimeTypes.json.value: {},
                    },
                    "model": Collections,
                },
            },
            response_class=GeoJSONResponse,
            endpoint=create_async_endpoint(self.client.post_all_collections, self.POST),
        )
        app.include_router(self.router)

    @classmethod
    def from_extensions(
        cls,
        extensions: List[ApiExtension],
        *,
        client: Union[AsyncBaseCollectionSearchClient, BaseCollectionSearchClient],
        settings: ApiSettings,
        schema_href: Optional[str] = None,
        router: Optional[APIRouter] = None,
    ) -> "CollectionSearchPostExtension":
        """Create CollectionSearchPostExtension object from extensions."""
        conformance_classes = [
            CollectionSearchConformanceClasses.COLLECTIONSEARCH,
            CollectionSearchConformanceClasses.BASIS,
        ]
        for ext in extensions:
            conformance_classes.extend(ext.conformance_classes)

        get_request_model = create_request_model(
            model_name="CollectionsGetRequest",
            base_model=BaseCollectionSearchGetRequest,
            extensions=extensions,
            request_type="GET",
        )

        post_request_model = create_request_model(
            model_name="CollectionsPostRequest",
            base_model=BaseCollectionSearchPostRequest,
            extensions=extensions,
            request_type="POST",
        )

        return cls(
            client=client,
            settings=settings,
            GET=get_request_model,
            POST=post_request_model,
            conformance_classes=conformance_classes,
            router=router or APIRouter(),
            schema_href=schema_href,
        )

"""Api request/response models."""

from typing import Annotated, Literal, cast

import attr
from fastapi import Path, Query
from pydantic import BaseModel, create_model
from stac_pydantic.shared import BBox

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.search import (
    APIRequest,
    BaseSearchGetRequest,
    BaseSearchPostRequest,
    DatetimeMixin,
    DateTimeQueryType,
    Limit,
    _bbox_converter,
    _validate_datetime,
)

try:
    import orjson  # noqa
    from fastapi.responses import ORJSONResponse as JSONResponse
except ImportError:  # pragma: nocover
    from starlette.responses import JSONResponse  # type: ignore [assignment]


def create_request_model(
    model_name="SearchGetRequest",
    base_model: type[BaseModel] | type[APIRequest] = BaseSearchGetRequest,
    extensions: list[ApiExtension] | None = None,
    mixins: list[type[BaseModel]] | list[type[APIRequest]] | None = None,
    request_type: str = "GET",
) -> type[BaseModel] | type[APIRequest]:
    """Create a pydantic model for validating request bodies."""
    fields = {}
    extension_models: list[type[BaseModel] | type[APIRequest]] = []

    # Check extensions for additional parameters to search
    for extension in extensions or []:
        if extension_model := extension.get_request_model(request_type):
            extension_models.append(extension_model)

    mixins = mixins or []

    models = [base_model] + extension_models + mixins

    # Handle GET requests
    if all([issubclass(m, APIRequest) for m in models]):
        get_model = attr.make_class(model_name, attrs={}, bases=tuple(models))
        return cast(type[APIRequest], get_model)

    # Handle POST requests
    elif all([issubclass(m, BaseModel) for m in models]):
        for model in models:
            for k, field_info in model.model_fields.items():  # type: ignore
                fields[k] = (field_info.annotation, field_info)

        post_model = create_model(model_name, **fields, __base__=base_model)  # type: ignore
        return cast(type[BaseModel], post_model)

    raise TypeError("Mixed Request Model types. Check extension request types.")


def create_get_request_model(
    extensions: list[ApiExtension] | None,
    base_model: type[APIRequest] = BaseSearchGetRequest,
) -> type[APIRequest]:
    """Wrap create_request_model to create the GET request model."""
    model = create_request_model(
        "SearchGetRequest",
        base_model=base_model,
        extensions=extensions,
        request_type="GET",
    )
    return cast(type[APIRequest], model)


def create_post_request_model(
    extensions: list[ApiExtension] | None,
    base_model: type[BaseModel] = BaseSearchPostRequest,
) -> type[BaseModel]:
    """Wrap create_request_model to create the POST request model."""
    model = create_request_model(
        "SearchPostRequest",
        base_model=base_model,
        extensions=extensions,
        request_type="POST",
    )
    return cast(type[BaseModel], model)


@attr.s
class CollectionUri(APIRequest):
    """Get or delete collection."""

    collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()


@attr.s
class ItemUri(APIRequest):
    """Get or delete item."""

    collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()
    item_id: Annotated[str, Path(description="Item ID")] = attr.ib()


@attr.s
class EmptyRequest(APIRequest):
    """Empty request."""

    ...


@attr.s
class ItemCollectionUri(APIRequest, DatetimeMixin):
    """Get item collection."""

    collection_id: Annotated[str, Path(description="Collection ID")] = attr.ib()
    limit: Annotated[
        Limit | None,
        Query(
            description="Limits the number of results that are included in each page of the response (capped to 10_000)."  # noqa: E501
        ),
    ] = attr.ib(default=10)
    bbox: BBox | None = attr.ib(default=None, converter=_bbox_converter)  # type: ignore [misc]
    datetime: DateTimeQueryType = attr.ib(default=None, validator=_validate_datetime)


class GeoJSONResponse(JSONResponse):
    """JSON with custom, vendor content-type."""

    media_type = "application/geo+json"


class JSONSchemaResponse(JSONResponse):
    """JSON with custom, vendor content-type."""

    media_type = "application/schema+json"


class HealthCheck(BaseModel, extra="allow"):
    """health check response model."""

    status: Literal["UP", "DOWN"]

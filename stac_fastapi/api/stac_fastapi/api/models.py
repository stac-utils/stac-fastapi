"""Api request/response models."""

import importlib.util
from typing import List, Optional, Type, Union

import attr
from fastapi import Path
from pydantic import BaseModel, create_model
from stac_pydantic.shared import BBox

from stac_fastapi.types.extension import ApiExtension
from stac_fastapi.types.rfc3339 import DateTimeType
from stac_fastapi.types.search import (
    APIRequest,
    BaseSearchGetRequest,
    BaseSearchPostRequest,
    str2bbox,
    str_to_interval,
)


def create_request_model(
    model_name="SearchGetRequest",
    base_model: Union[Type[BaseModel], APIRequest] = BaseSearchGetRequest,
    extensions: Optional[List[ApiExtension]] = None,
    mixins: Optional[Union[List[BaseModel], List[APIRequest]]] = None,
    request_type: Optional[str] = "GET",
) -> Union[Type[BaseModel], APIRequest]:
    """Create a pydantic model for validating request bodies."""
    fields = {}
    extension_models = []

    # Check extensions for additional parameters to search
    for extension in extensions or []:
        if extension_model := extension.get_request_model(request_type):
            extension_models.append(extension_model)

    mixins = mixins or []

    models = [base_model] + extension_models + mixins

    # Handle GET requests
    if all([issubclass(m, APIRequest) for m in models]):
        return attr.make_class(model_name, attrs={}, bases=tuple(models))

    # Handle POST requests
    elif all([issubclass(m, BaseModel) for m in models]):
        for model in models:
            for k, field_info in model.model_fields.items():
                fields[k] = (field_info.annotation, field_info)
        return create_model(model_name, **fields, __base__=base_model)

    raise TypeError("Mixed Request Model types. Check extension request types.")


def create_get_request_model(
    extensions: Optional[List[ApiExtension]],
    base_model: BaseSearchGetRequest = BaseSearchGetRequest,
) -> APIRequest:
    """Wrap create_request_model to create the GET request model."""

    return create_request_model(
        "SearchGetRequest",
        base_model=base_model,
        extensions=extensions,
        request_type="GET",
    )


def create_post_request_model(
    extensions: Optional[List[ApiExtension]],
    base_model: BaseSearchPostRequest = BaseSearchPostRequest,
) -> Type[BaseModel]:
    """Wrap create_request_model to create the POST request model."""
    return create_request_model(
        "SearchPostRequest",
        base_model=base_model,
        extensions=extensions,
        request_type="POST",
    )


@attr.s  # type:ignore
class CollectionUri(APIRequest):
    """Get or delete collection."""

    collection_id: str = attr.ib(default=Path(..., description="Collection ID"))


@attr.s
class ItemUri(CollectionUri):
    """Get or delete item."""

    item_id: str = attr.ib(default=Path(..., description="Item ID"))


@attr.s
class EmptyRequest(APIRequest):
    """Empty request."""

    ...


@attr.s
class ItemCollectionUri(CollectionUri):
    """Get item collection."""

    limit: int = attr.ib(default=10)
    bbox: Optional[BBox] = attr.ib(default=None, converter=str2bbox)
    datetime: Optional[DateTimeType] = attr.ib(default=None, converter=str_to_interval)


class POSTTokenPagination(BaseModel):
    """Token pagination model for POST requests."""

    token: Optional[str] = None


@attr.s
class GETTokenPagination(APIRequest):
    """Token pagination for GET requests."""

    token: Optional[str] = attr.ib(default=None)


class POSTPagination(BaseModel):
    """Page based pagination for POST requests."""

    page: Optional[str] = None


@attr.s
class GETPagination(APIRequest):
    """Page based pagination for GET requests."""

    page: Optional[str] = attr.ib(default=None)


# Test for ORJSON and use it rather than stdlib JSON where supported
if importlib.util.find_spec("orjson") is not None:
    from fastapi.responses import ORJSONResponse

    class GeoJSONResponse(ORJSONResponse):
        """JSON with custom, vendor content-type."""

        media_type = "application/geo+json"

    class JSONSchemaResponse(ORJSONResponse):
        """JSON with custom, vendor content-type."""

        media_type = "application/schema+json"

else:
    from starlette.responses import JSONResponse

    class GeoJSONResponse(JSONResponse):
        """JSON with custom, vendor content-type."""

        media_type = "application/geo+json"

    class JSONSchemaResponse(JSONResponse):
        """JSON with custom, vendor content-type."""

        media_type = "application/schema+json"

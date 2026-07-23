# Tips and Tricks

This page contains a few 'tips and tricks' for getting **stac-fastapi** working in various situations.

## Avoid FastAPI (slow) serialization

When not using Pydantic validation for responses, FastAPI will still use a complex (slow) [serialization process](https://github.com/fastapi/fastapi/discussions/8165).

Starting with stac-fastapi `5.2.0`, we've added `ENABLE_DIRECT_RESPONSE` option to by-pass the default FastAPI serialization by wrapping the endpoint responses into `starlette.Response` classes.

Ref: https://github.com/stac-utils/stac-fastapi-elasticsearch-opensearch/issues/347

## Application Middlewares

By default the `StacApi` class will enable 3 Middlewares (`BrotliMiddleware`, `CORSMiddleware` and `ProxyHeaderMiddleware`). You may want to overwrite the defaults configuration by editing your backend's `app.py`:

```python
from starlette.middleware import Middleware

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.middleware import CORSMiddleware

api = StacApi(
    ...
    middlewares=[
        Middleware(CORSMiddleware, allow_origins=["https://myendpoints.io"])
    ],
    ...
)
```

## Default `includes` in Fields extension (POST request)

The [**Fields** API extension](https://github.com/stac-api-extensions/fields) enables to filter in/out STAC Items keys (e.g `geometry`). The default behavior is to not filter out anything, but this can be overridden by providing a custom `FieldsExtensionPostRequest` class:

```python
from typing import Optional, Set

import attr
from stac_fastapi.extensions import FieldsExtension as FieldsExtensionBase
from stac_fastapi.extensions.fields import request
from pydantic import BaseModel, Field


class PostFieldsExtension(requests.PostFieldsExtension):
    include: Optional[Set[str]] = Field(
        default_factory=lambda: {
            "id",
            "type",
            "stac_version",
            "geometry",
            "bbox",
            "links",
            "assets",
            "properties.datetime",
            "collection",
        }
    )
    exclude: Optional[Set[str]] = set()


class FieldsExtensionPostRequest(BaseModel):
    """Additional fields and schema for the POST request."""

    fields: Optional[PostFieldsExtension] = Field(PostFieldsExtension())


class FieldsExtension(FieldsExtensionBase):
    """Override the POST model"""

    POST = FieldsExtensionPostRequest


from stac_fastapi.api.app import StacApi

stac = StacApi(
    extensions=[
        FieldsExtension()
    ]
)
```

## Custom Sortables client

The Sort extension v1.1.0 adds `sortables` endpoints so clients can discover which fields are available for sorting. The base `SortExtension` mounts `/sortables`, `/collections/{collection_id}/sortables`, and `/collections-sortables`, but only when a `BaseSortablesClient` (or `AsyncBaseSortablesClient`) is provided.

```python
from typing import Any

from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.sort import BaseSortablesClient, SortExtension


class MySortablesClient(BaseSortablesClient):
    def get_sortables(self, **kwargs: Any) -> dict[str, Any]:
        return {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$id": "https://example.com/sortables",
            "type": "object",
            "title": "Sortables",
            "properties": {
                "datetime": {"type": "string", "format": "date-time"},
            },
            "additionalProperties": True,
        }

    # get_collection_sortables and get_collections_sortables can be
    # overridden in the same way.


stac = StacApi(
    extensions=[
        SortExtension(client=MySortablesClient()),
    ]
)
```

Use `SearchSortExtension`, `ItemCollectionSortExtension`, or `CollectionSearchSortExtension` if you only need sortables for a particular set of endpoints.

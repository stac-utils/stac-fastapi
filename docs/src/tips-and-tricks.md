# Tips and Tricks

This page contains a few 'tips and tricks' for getting **stac-fastapi** working in various situations.

## Get stac-fastapi working with CORS

CORS (Cross-Origin Resource Sharing) support may be required to use stac-fastapi in certain situations.
For example, if you are running [stac-browser](https://github.com/radiantearth/stac-browser) to browse the STAC catalog created by **stac-fastapi**, then you will need to enable CORS support.
To do this, edit your backend's `app.py` and add the following import:

```python
from fastapi.middleware.cors import CORSMiddleware
```

and then edit the `api = StacApi(...` call to add the following parameter:

```python
middlewares=[lambda app: CORSMiddleware(app, allow_origins=["*"])]
```

If needed, you can edit the `allow_origins` parameter to only allow CORS requests from specific origins.

## Set API title, description and version

For the landing page, you can set the API title, description and version using environment variables.

- `STAC_FASTAPI_VERSION` (string) is the version number of your API instance (this is not the STAC version).
- `STAC FASTAPI_TITLE` (string) should be a self-explanatory title for your API.
- `STAC FASTAPI_DESCRIPTION` (string) should be a good description for your API. It can contain CommonMark.
- `STAC_FASTAPI_LANDING_ID` (string) is a unique identifier for your Landing page.


## Default `includes` in Fields extension (POST request)

The [**Fields** API extension](https://github.com/stac-api-extensions/fields) enables to filter in/out STAC Items keys (e.g `geometry`). The default behavior is to not filter out anything, but this can be overridden by providing a custom `FieldsExtensionPostRequest` class:

```python
from typing import Optional, Set

import attr
from stac_fastapi.extensions.core import FieldsExtension as FieldsExtensionBase
from stac_fastapi.extensions.core.fields import request
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

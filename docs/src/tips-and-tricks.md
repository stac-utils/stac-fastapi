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

## Enable the Context extension

!!! Warning

    The `ContextExtension` is deprecated and will be removed in 3.0. See https://github.com/radiantearth/stac-api-spec/issues/396

The Context STAC extension provides information on the number of items matched and returned from a STAC search.
This is required by various other STAC-related tools, such as the pystac command-line client.
To enable the extension, edit your backend's `app.py` and add the following import:

```python
from stac_fastapi.extensions.core.context import ContextExtension
```


and then edit the `api = StacApi(...` call to add `ContextExtension()` to the list given as the `extensions` parameter.

## Set API title, description and version

For the landing page, you can set the API title, description and version using environment variables.

- `STAC_FASTAPI_VERSION` (string) is the version number of your API instance (this is not the STAC version).
- `STAC FASTAPI_TITLE` (string) should be a self-explanatory title for your API.
- `STAC FASTAPI_DESCRIPTION` (string) should be a good description for your API. It can contain CommonMark.
- `STAC_FASTAPI_LANDING_ID` (string) is a unique identifier for your Landing page.

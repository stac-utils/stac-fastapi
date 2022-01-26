# Tips and Tricks
This page contains a few 'tips and tricks' for getting stac-fastapi working in various situations.

## Get stac-fastapi working with CORS
CORS (Cross-Origin Resource Sharing) support may be required to use stac-fastapi in certain situations. For example, if you are running
[stac-browser](https://github.com/radiantearth/stac-browser) to browse the STAC catalog created by stac-fastapi, then you will need to enable CORS support.

To do this, create a JSON configuration file whose schema matches the options described in the [FastAPI docs](https://fastapi.tiangolo.com/tutorial/cors/), e.g.

```
{
    "allow_origins": ["*"],
    "allow_methods": ["*"]
}
```

Deploy this file to a location accessible by stac-fastapi, e.g. in Dockerfile

```
RUN mkdir /config
COPY cors.json /config/cors.json
```

Set an environment variable `CORS_CONFIG_LOCATION` pointing to this file, e.g. in Dockerfile

```
ENV CORS_CONFIG_LOCATION=/config/cors.json
```

If needed, you can edit the `allow_origins` parameter to only allow CORS requests from specific origins.

## Enable the Context extension
The Context STAC extension provides information on the number of items matched and returned from a STAC search. This is required by various other STAC-related tools, such as the pystac command-line client. To enable the extension, edit `stac_fastapi/sqlalchemy/stac_fastapi/sqlalchemy/app.py` (or the equivalent in the `pgstac` folder) and add the following import:

```
from stac_fastapi.extensions.core.context import ContextExtension
```

and then edit the `api = StacApi(...` call to add `ContextExtension()` to the list given as the `extensions` parameter.
# Tips and Tricks
This page contains a few 'tips and tricks' for getting stac-fastapi working in various situations.

## Get stac-fastapi working with CORS
CORS (Cross-Origin Resource Sharing) support may be required to use stac-fastapi in certain situations. For example, if you are running
[stac-browser](https://github.com/radiantearth/stac-browser) to browse the STAC catalog created by stac-fastapi, then you will need to enable CORS support.

To do this, configure environment variables for the configuration options described in [FastAPI docs](https://fastapi.tiangolo.com/tutorial/cors/) using a `cors_` prefix e.g.
```
cors_allow_credentials=true [or 1]
```
Sequences, such as `allow_origins`, should be in JSON format e.g.
```
cors_allow_origins='["http://domain.one", "http://domain.two"]'
```

## Enable the Context extension
The Context STAC extension provides information on the number of items matched and returned from a STAC search. This is required by various other STAC-related tools, such as the pystac command-line client. To enable the extension, edit `stac_fastapi/sqlalchemy/stac_fastapi/sqlalchemy/app.py` (or the equivalent in the `pgstac` folder) and add the following import:

```
from stac_fastapi.extensions.core.context import ContextExtension
```

and then edit the `api = StacApi(...` call to add `ContextExtension()` to the list given as the `extensions` parameter.
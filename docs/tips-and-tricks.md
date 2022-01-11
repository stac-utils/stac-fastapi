# Tips and Tricks
This page contains a few 'tips and tricks' for getting stac-fastapi working in various situations.

## Get stac-fastapi working with CORS
CORS (Cross-Origin Resource Sharing) support may be required to use stac-fastapi in certain situations. For example, if you are running
[stac-browser](https://github.com/radiantearth/stac-browser) to browse the STAC catalog created by stac-fastapi, then you will need to enable CORS support.

To do this, edit `stac_fastapi/sqlalchemy/stac_fastapi/sqlalchemy/app.py` (or the equivalent in the `pgstac` folder) and add the following import:

```
from fastapi.middleware.cors import CORSMiddleware
```

and then edit the `api = StacApi(...` call to add the following parameter:

```
middlewares=[lambda app: CORSMiddleware(app, allow_origins=["*"])]
```

If needed, you can edit the `allow_origins` parameter to only allow CORS requests from specific origins.

## Enable the Context extension
The Context STAC extension provides information on the number of items matched and returned from a STAC search. This is required by various other STAC-related tools, such as the pystac command-line client. To enable the extension, edit `stac_fastapi/sqlalchemy/stac_fastapi/sqlalchemy/app.py` (or the equivalent in the `pgstac` folder) and add the following import:

```
from stac_fastapi.extensions.core.context import ContextExtension
```

and then edit the `api = StacApi(...` call to add `ContextExtension()` to the list given as the `extensions` parameter.
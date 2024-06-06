"""Filter extensions clients."""

import abc
from typing import Any, Dict, Optional

import attr


@attr.s
class AsyncBaseFiltersClient(abc.ABC):
    """Defines a pattern for implementing the STAC filter extension."""

    async def get_queryables(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """Get the queryables available for the given collection_id.

        If collection_id is None, returns the intersection of all queryables over all
        collections.

        This base implementation returns a blank queryable schema. This is not allowed
        under OGC CQL but it is allowed by the STAC API Filter Extension
        https://github.com/radiantearth/stac-api-spec/tree/master/fragments/filter#queryables
        """
        return {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "https://example.org/queryables",
            "type": "object",
            "title": "Queryables for Example STAC API",
            "description": "Queryable names for the example STAC API Item Search filter.",
            "properties": {},
        }


@attr.s
class BaseFiltersClient(abc.ABC):
    """Defines a pattern for implementing the STAC filter extension."""

    def get_queryables(
        self, collection_id: Optional[str] = None, **kwargs
    ) -> Dict[str, Any]:
        """Get the queryables available for the given collection_id.

        If collection_id is None, returns the intersection of all queryables over all
        collections.

        This base implementation returns a blank queryable schema. This is not allowed
        under OGC CQL but it is allowed by the STAC API Filter Extension
        https://github.com/stac-api-extensions/filter#queryables
        """
        return {
            "$schema": "https://json-schema.org/draft/2019-09/schema",
            "$id": "https://example.org/queryables",
            "type": "object",
            "title": "Queryables for Example STAC API",
            "description": "Queryable names for the example STAC API Item Search filter.",
            "properties": {},
        }

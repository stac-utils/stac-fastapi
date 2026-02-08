"""Catalogs extension types."""

from typing import Any, Dict, List, Optional

from stac_pydantic.catalog import Catalog
from stac_pydantic.links import Links
from stac_pydantic.shared import StacBaseModel


class Catalogs(StacBaseModel):
    """Catalogs endpoint response.

    Similar to Collections but for catalogs.
    """

    catalogs: List[Catalog]
    links: Links
    numberMatched: Optional[int] = None
    numberReturned: Optional[int] = None


class Children(StacBaseModel):
    """Children endpoint response.

    Returns a mixed list of Catalogs and Collections as children.
    """

    children: List[Dict[str, Any]]
    links: Links
    numberMatched: Optional[int] = None
    numberReturned: Optional[int] = None

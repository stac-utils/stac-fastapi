"""Catalogs extension types."""

from typing import List

from pydantic import BaseModel
from stac_pydantic.catalog import Catalog
from stac_pydantic.collection import Collection
from stac_pydantic.links import Links
from stac_pydantic.shared import StacBaseModel


class ObjectUri(BaseModel):
    """Simple model for linking existing resources by ID.

    Used for Mode B (Linking) operations where only the ID is provided
    to reference an existing catalog or collection.
    """

    id: str


class Catalogs(StacBaseModel):
    """Catalogs endpoint response."""

    catalogs: List[Catalog]
    links: Links
    numberMatched: int | None = None
    numberReturned: int | None = None


class Children(StacBaseModel):
    """Children endpoint response.

    Returns a mixed list of Catalogs and Collections as children.
    """

    children: List[Catalog | Collection]
    links: Links
    numberMatched: int | None = None
    numberReturned: int | None = None

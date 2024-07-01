"""Pagination extension request models."""

from typing import Optional

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class GETTokenPagination(APIRequest):
    """Token pagination for GET requests."""

    token: Optional[str] = attr.ib(default=None)


class POSTTokenPagination(BaseModel):
    """Token pagination model for POST requests."""

    token: Optional[str] = None


@attr.s
class GETPagination(APIRequest):
    """Page based pagination for GET requests."""

    page: Optional[str] = attr.ib(default=None)


class POSTPagination(BaseModel):
    """Page based pagination for POST requests."""

    page: Optional[str] = None

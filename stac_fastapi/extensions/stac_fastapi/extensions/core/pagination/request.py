"""Pagination extension request models."""

from typing import Optional

import attrs
from fastapi import Query
from pydantic import BaseModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@attrs.define(slots=False)
class GETTokenPagination(APIRequest):
    """Token pagination for GET requests."""

    token: Annotated[Optional[str], Query()] = attrs.field(default=None)


class POSTTokenPagination(BaseModel):
    """Token pagination model for POST requests."""

    token: Optional[str] = None


@attrs.define(slots=False)
class GETPagination(APIRequest):
    """Page based pagination for GET requests."""

    page: Annotated[Optional[str], Query()] = attrs.field(default=None)


class POSTPagination(BaseModel):
    """Page based pagination for POST requests."""

    page: Optional[str] = None


@attrs.define(slots=False)
class GETOffsetPagination(APIRequest):
    """Offset pagination for GET requests."""

    offset: Annotated[Optional[int], Query()] = attrs.field(default=None)


class POSTOffsetPagination(BaseModel):
    """Offset pagination model for POST requests."""

    offset: Optional[int] = None

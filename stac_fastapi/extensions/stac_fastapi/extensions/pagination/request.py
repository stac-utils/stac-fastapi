"""Pagination extension request models."""

from typing import Annotated

import attr
from fastapi import Query
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class GETTokenPagination(APIRequest):
    """Token pagination for GET requests."""

    token: Annotated[str | None, Query()] = attr.ib(default=None)


class POSTTokenPagination(BaseModel):
    """Token pagination model for POST requests."""

    token: str | None = None


@attr.s
class GETPagination(APIRequest):
    """Page based pagination for GET requests."""

    page: Annotated[str | None, Query()] = attr.ib(default=None)


class POSTPagination(BaseModel):
    """Page based pagination for POST requests."""

    page: str | None = None


@attr.s
class GETOffsetPagination(APIRequest):
    """Offset pagination for GET requests."""

    offset: Annotated[int | None, Query()] = attr.ib(default=None)


class POSTOffsetPagination(BaseModel):
    """Offset pagination model for POST requests."""

    offset: int | None = None

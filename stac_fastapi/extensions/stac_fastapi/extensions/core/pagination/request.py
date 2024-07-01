"""Pagination extension request models."""

from dataclasses import dataclass
from typing import Optional

from fastapi import Query
from pydantic import BaseModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest


@dataclass
class GETTokenPagination(APIRequest):
    """Token pagination for GET requests."""

    token: Annotated[Optional[str], Query()] = None


class POSTTokenPagination(BaseModel):
    """Token pagination model for POST requests."""

    token: Optional[str] = None


@dataclass
class GETPagination(APIRequest):
    """Page based pagination for GET requests."""

    page: Annotated[Optional[str], Query()] = None


class POSTPagination(BaseModel):
    """Page based pagination for POST requests."""

    page: Optional[str] = None

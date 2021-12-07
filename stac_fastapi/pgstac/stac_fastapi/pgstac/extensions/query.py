"""Pgstac query customisation."""

import operator
from enum import auto
from types import DynamicClassAttribute
from typing import Any, Callable, Dict, Optional

from pydantic import BaseModel
from stac_pydantic.utils import AutoValueEnum

from stac_fastapi.extensions.core.query import QueryExtension as QueryExtensionBase


class Operator(str, AutoValueEnum):
    """Defines the set of operators supported by the API."""

    eq = auto()
    ne = auto()
    lt = auto()
    lte = auto()
    gt = auto()
    gte = auto()
    # TODO: These are defined in the spec but aren't currently implemented by the api
    # startsWith = auto()
    # endsWith = auto()
    # contains = auto()
    # in = auto()

    @DynamicClassAttribute
    def operator(self) -> Callable[[Any, Any], bool]:
        """Return python operator."""
        return getattr(operator, self._value_)


class QueryExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    query: Optional[Dict[str, Dict[Operator, Any]]]


class QueryExtension(QueryExtensionBase):
    """Query Extension.

    Override the POST request model to add validation against
    supported fields
    """

    POST = QueryExtensionPostRequest

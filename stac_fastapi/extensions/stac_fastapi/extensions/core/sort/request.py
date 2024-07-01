# encoding: utf-8
"""Request model for the Sort Extension."""

from dataclasses import dataclass
from typing import List, Optional

from fastapi import Query
from pydantic import BaseModel
from stac_pydantic.api.extensions.sort import SortExtension as PostSortModel
from typing_extensions import Annotated

from stac_fastapi.types.search import APIRequest, str2list


@dataclass
class SortExtensionGetRequest(APIRequest):
    """Sortby Parameter for GET requests."""

    sortby: Annotated[Optional[str], Query()] = None

    def __post_init__(self):
        """convert attributes."""
        if self.sortby:
            self.sortby = str2list(self.sortby)  # type: ignore


class SortExtensionPostRequest(BaseModel):
    """Sortby parameter for POST requests."""

    sortby: Optional[List[PostSortModel]] = None

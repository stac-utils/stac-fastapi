# encoding: utf-8
"""Request model for the Sort Extension."""

from typing import List, Optional

import attr
from pydantic import BaseModel
from stac_pydantic.api.extensions.sort import SortExtension as PostSortModel

from stac_fastapi.types.search import APIRequest, str2list


@attr.s
class SortExtensionGetRequest(APIRequest):
    """Sortby Parameter for GET requests."""

    sortby: Optional[str] = attr.ib(default=None, converter=str2list)


class SortExtensionPostRequest(BaseModel):
    """Sortby parameter for POST requests."""

    sortby: Optional[List[PostSortModel]] = None

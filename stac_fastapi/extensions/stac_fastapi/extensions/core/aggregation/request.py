"""Request model for the Aggregation extension."""

from typing import Any, Dict, Optional, Union, List

import attr
from pydantic import BaseModel

from stac_fastapi.types.search import APIRequest


@attr.s
class AggregationExtensionGetRequest(APIRequest):
    """Query Extension GET request model."""

    aggregations: Optional[Union[str, List[str]]] = attr.ib(default=None)
    grid_geohex_frequency_precision: Optional[Union[str, int]] = attr.ib(default=None) 
    # add the others   


class AggregateExtensionPostRequest(BaseModel):
    """Query Extension POST request model."""

    aggregations: Optional[Union[str, List[str]]] = attr.ib(default=None)
    grid_geohex_frequency_precision: Optional[Union[str, int]] = attr.ib(default=None)    
    # add the others


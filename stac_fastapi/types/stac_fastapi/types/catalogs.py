# Cloned from stac_pydantic.api.collections v2.0

from typing import List

from pydantic import BaseModel

from stac_pydantic import Catalog
from stac_pydantic.api.links import Link


class Catalogs(BaseModel):
    """
    http://docs.opengeospatial.org/is/17-069r3/17-069r3.html#_feature_collections_rootcollections
    """

    links: List[Link]
    collections: List[Catalog]

    def to_dict(self, **kwargs):
        return self.dict(by_alias=True, exclude_unset=True, **kwargs)

    def to_json(self, **kwargs):
        return self.json(by_alias=True, exclude_unset=True, **kwargs)
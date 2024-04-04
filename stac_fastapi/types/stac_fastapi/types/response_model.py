"""Response models for STAC FastAPI.
Depending on settings models are either TypeDicts or Pydantic models."""

from stac_pydantic import api

from stac_fastapi.types import stac
from stac_fastapi.types.config import ApiSettings

settings = ApiSettings()

if settings.validate_response:
    response_model = api
else:
    response_model = stac


LandingPage = response_model.LandingPage
Collection = response_model.Collection
Collections = response_model.Collections
Item = response_model.Item
ItemCollection = response_model.ItemCollection
try:
    Conformance = response_model.Conformance
except AttributeError:
    # TODO: class name needs to be fixed in stac_pydantic
    # stac-utils/stac-pydantic#136
    Conformance = response_model.ConformanceClasses

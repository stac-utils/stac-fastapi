"""API configuration."""
from typing import Set

from stac_fastapi.types.config import ApiSettings


class MongoSettings(ApiSettings):
    """API settings."""

    # Fields which are defined by STAC but not included in the database model
    forbidden_fields: Set[str] = {"type"}

    # Fields which are item properties but indexed as distinct fields in the database model
    indexed_fields: Set[str] = {"datetime"}

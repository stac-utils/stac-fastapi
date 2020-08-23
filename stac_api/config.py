"""Application settings."""
import enum
from typing import List, Optional, Set

from pydantic import BaseSettings


# TODO: Move to stac-pydantic
class ApiExtensions(enum.Enum):
    """
    Enumeration of available stac api extensions
    Ref: https://github.com/radiantearth/stac-api-spec/tree/master/extensions
    """

    context = "context"
    fields = "fields"
    query = "query"
    sort = "sort"
    transaction = "transaction"


class ApiSettings(BaseSettings):
    """Application settings"""

    environment: str
    debug: bool = False
    postgres_user: str
    postgres_pass: str
    postgres_host_reader: str
    postgres_host_writer: str
    postgres_port: str
    postgres_dbname: str

    # Enabled api extensions
    stac_api_extensions: Optional[List[ApiExtensions]] = None

    # Fields which are defined by STAC but not included in the database model
    forbidden_fields: Set[str] = {"type", "stac_version"}

    # Fields which are item properties but indexed as distinct fields in the database model
    indexed_fields: Set[str] = {"datetime"}

    # Fields which are always included in the response (fields extension)
    default_includes: Set[str] = {
        "id",
        "type",
        "geometry",
        "bbox",
        "links",
        "assets",
        "properties.datetime",
    }

    class Config:
        """model config"""

        env_file = ".env"

    @property
    def reader_connection_string(self):
        """Create reader psql connection string"""
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_reader}:{self.postgres_port}/{self.postgres_dbname}"

    @property
    def writer_connection_string(self):
        """Create writer psql connection string"""
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_writer}:{self.postgres_port}/{self.postgres_dbname}"

    def is_enabled(self, ext: ApiExtensions) -> bool:
        """Helper method to check if an api extension is enabled"""
        return ext in self.stac_api_extensions or False


settings: Optional[ApiSettings] = None


def inject_settings(base_settings: ApiSettings):
    """Inject settings to global scope"""
    global settings
    settings = base_settings

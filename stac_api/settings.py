from typing import Set

from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    environment: str
    debug: bool = False
    postgres_user: str
    postgres_pass: str
    postgres_host_reader: str
    postgres_host_writer: str
    postgres_port: str
    postgres_dbname: str

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
        env_file = ".env"

    @property
    def reader_connection_string(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_reader}:{self.postgres_port}/{self.postgres_dbname}"

    @property
    def writer_connection_string(self):
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_writer}:{self.postgres_port}/{self.postgres_dbname}"


settings = ApiSettings()

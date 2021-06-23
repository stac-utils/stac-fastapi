"""Postgres API configuration."""

from stac_fastapi.types.config import ApiSettings


class Settings(ApiSettings):
    """Postgres-specific API settings.

    Attributes:
        postgres_user: postgres username.
        postgres_pass: postgres password.
        postgres_host_reader: hostname for the reader connection.
        postgres_host_writer: hostname for the writer connection.
        postgres_port: database port.
        postgres_dbname: database name.
    """

    postgres_user: str
    postgres_pass: str
    postgres_host_reader: str
    postgres_host_writer: str
    postgres_port: str
    postgres_dbname: str

    db_min_conn_size: int = 10
    db_max_conn_size: int = 10
    db_max_queries: int = 50000
    db_max_inactive_conn_lifetime: float = 300

    testing: bool = False

    @property
    def reader_connection_string(self):
        """Create reader psql connection string."""
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_reader}:{self.postgres_port}/{self.postgres_dbname}"

    @property
    def writer_connection_string(self):
        """Create writer psql connection string."""
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_writer}:{self.postgres_port}/{self.postgres_dbname}"

    @property
    def testing_connection_string(self):
        """Create testing psql connection string."""
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host_writer}:{self.postgres_port}/pgstactestdb"

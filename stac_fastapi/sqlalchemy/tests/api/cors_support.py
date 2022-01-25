from json import dumps
from os import environ, fdopen, path, sep
from tempfile import mkstemp
from typing import Final

cors_config_location_key: Final = "CORS_CONFIG_LOCATION"
cors_permit_origin: Final = "http://cors.pass"
cors_deny_origin: Final = "http://cors.fail"


def cors_enable():
    tmp_file, tmp_filename = mkstemp()
    with fdopen(tmp_file, "w") as f:
        f.write(dumps({"allow_origins": [cors_permit_origin]}))
    environ[cors_config_location_key] = tmp_filename


def cors_disable() -> None:
    environ.pop(cors_config_location_key, None)


def cors_missing():
    environ[cors_config_location_key] = path.join(path.abspath(sep), "missing.file")

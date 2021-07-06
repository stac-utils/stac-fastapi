"""Ingest sample data during docker-compose"""
import json
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

workingdir = Path(__file__).parent.absolute()
joplindata = workingdir.parent / "stac_fastapi" / "testdata" / "joplin"

app_host = sys.argv[1]

retry_strategy = Retry(connect=5, backoff_factor=2)
adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)
session.mount("http://", adapter)

if not app_host:
    raise Exception("You must include full path/port to stac instance")


def ingest_joplin_data(app_host: str = app_host, data_dir: Path = joplindata):
    """ingest data."""

    with open(data_dir / "collection.json") as f:
        collection = json.load(f)

    r = session.post(urljoin(app_host, "collections"), json=collection)
    if r.status_code not in (200, 409):
        r.raise_for_status()

    with open(data_dir / "index.geojson") as f:
        index = json.load(f)

    for feat in index["features"]:
        del feat["stac_extensions"]
        r = session.post(
            urljoin(app_host, f"collections/{collection['id']}/items"), json=feat
        )
        if r.status_code == 409:
            continue
        r.raise_for_status()


if __name__ == "__main__":
    ingest_joplin_data()

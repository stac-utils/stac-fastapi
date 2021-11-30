"""Ingest sample data during docker-compose"""
import json
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests

workingdir = Path(__file__).parent.absolute()
joplindata = workingdir.parent / "stac_fastapi" / "testdata" / "joplin"

app_host = sys.argv[1]

if not app_host:
    raise Exception("You must include full path/port to stac instance")


def post_or_put(url: str, data: dict):
    """Post or put data to url."""
    r = requests.post(url, json=data)
    if r.status_code == 409:
        # Exists, so update
        r = requests.put(url, json=data)
        # Unchanged may throw a 404
        if not r.status_code == 404:
            r.raise_for_status()
    else:
        r.raise_for_status()


def ingest_joplin_data(app_host: str = app_host, data_dir: Path = joplindata):
    """ingest data."""

    with open(data_dir / "collection.json") as f:
        collection = json.load(f)

    post_or_put(urljoin(app_host, "/collections"), collection)

    with open(data_dir / "index.geojson") as f:
        index = json.load(f)

    for feat in index["features"]:
        del feat["stac_extensions"]
        post_or_put(urljoin(app_host, f"collections/{collection['id']}/items"), feat)


if __name__ == "__main__":
    ingest_joplin_data()

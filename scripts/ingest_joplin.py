"""Ingest sample data during docker-compose"""
import json
from pathlib import Path
from urllib.parse import urljoin

import requests

bucket = "arturo-stac-api-test-data"
app_host = "http://app:8081"


def ingest_joplin_data(data_dir=Path.cwd() / "tests" / "data" / "joplin"):
    """ingest data."""

    with open(data_dir / "collection.json") as f:
        collection = json.load(f)

    r = requests.post(urljoin(app_host, "collections"), json=collection)
    if r.status_code not in (200, 409):
        r.raise_for_status()

    with open(data_dir / "index.geojson") as f:
        index = json.load(f)

    for feat in index["features"]:
        del feat["stac_extensions"]
        r = requests.post(
            urljoin(app_host, f"collections/{collection['id']}/items"), json=feat
        )
        if r.status_code == 409:
            continue
        r.raise_for_status()


if __name__ == "__main__":
    ingest_joplin_data()

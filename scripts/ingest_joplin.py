"""Ingest sample data during docker-compose"""

from urllib.parse import urljoin

import requests

bucket = "arturo-stac-api-test-data"
app_host = "http://host.docker.internal:8081"


def ingest_joplin_data():
    """ingest data"""
    r = requests.get(f"https://{bucket}.s3.amazonaws.com/joplin/collection.json")
    collection = r.json()

    r = requests.post(urljoin(app_host, "/collections"), json=collection)
    if r.status_code not in (200, 409):
        r.raise_for_status()

    r = requests.get(f"https://{bucket}.s3.amazonaws.com/joplin/index.geojson")
    index = r.json()
    for feat in index["features"]:
        del feat["stac_extensions"]
        r = requests.post(
            urljoin(app_host, f"/collections/{collection['id']}/items"), json=feat
        )
        if r.status_code == 409:
            continue
        r.raise_for_status()


if __name__ == "__main__":
    ingest_joplin_data()

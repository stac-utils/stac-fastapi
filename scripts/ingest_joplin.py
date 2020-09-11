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
    r.raise_for_status()

    r = requests.get(f"https://{bucket}.s3.amazonaws.com/joplin/index.geojson")
    index = r.json()
    for feat in index["features"]:
        r = requests.post(
            urljoin(app_host, f"/collections/{collection['id']}/items"), json=feat
        )
        r.raise_for_status()


if __name__ == "__main__":
    ingest_joplin_data()

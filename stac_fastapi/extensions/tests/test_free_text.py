# noqa: E501
"""test freetext extension."""


from starlette.testclient import TestClient

from stac_fastapi.api.app import StacApi
from stac_fastapi.api.models import (
    ItemCollectionUri,
    create_get_request_model,
    create_post_request_model,
    create_request_model,
)
from stac_fastapi.extensions.core import FreeTextAdvancedExtension, FreeTextExtension
from stac_fastapi.extensions.core.free_text import FreeTextConformanceClasses
from stac_fastapi.types.config import ApiSettings
from stac_fastapi.types.core import BaseCoreClient


class DummyCoreClient(BaseCoreClient):
    def all_collections(self, *args, **kwargs):
        return kwargs.pop("q", None)

    def get_collection(self, *args, **kwargs):
        raise NotImplementedError

    def get_item(self, *args, **kwargs):
        raise NotImplementedError

    def get_search(self, *args, **kwargs):
        return kwargs.pop("q", None)

    def post_search(self, *args, **kwargs):
        return args[0].q

    def item_collection(self, *args, **kwargs):
        return kwargs.pop("q", None)


def test_search_free_text_search():
    """Test search endpoints with free-text ext."""
    settings = ApiSettings()
    extensions = [
        FreeTextExtension(conformance_classes=[FreeTextConformanceClasses.SEARCH])
    ]

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=extensions,
        search_get_request_model=create_get_request_model(extensions),
        search_post_request_model=create_post_request_model(extensions),
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        conforms = response_dict["conformsTo"]
        assert FreeTextConformanceClasses.SEARCH in conforms

        # /search - GET, no free-text
        response = client.get(
            "/search",
            params={"collections": ["test"]},
        )
        assert response.is_success
        assert not response.text

        # /search - GET, free-text option
        response = client.get(
            "/search",
            params={
                "collections": ["test"],
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == ["ocean", "coast"]

        # /search - POST, no free-text
        response = client.post(
            "/search",
            json={
                "collections": ["test"],
            },
        )
        assert response.is_success
        assert not response.text

        # /search - POST, free-text option
        response = client.post(
            "/search",
            json={
                "collections": ["test"],
                "q": ["ocean", "coast"],
            },
        )

        assert response.is_success, response.text
        assert response.json() == ["ocean", "coast"]


def test_search_free_text_complete():
    """Test search,collections,items endpoints with free-text ext."""
    settings = ApiSettings()

    free_text = FreeTextExtension(
        conformance_classes=[
            FreeTextConformanceClasses.SEARCH,
            FreeTextConformanceClasses.ITEMS,
            FreeTextConformanceClasses.COLLECTIONS,
        ]
    )

    search_get_model = create_get_request_model([free_text])
    search_post_model = create_post_request_model([free_text])
    items_get_model = create_request_model(
        "ItemCollectionURI",
        base_model=ItemCollectionUri,
        mixins=[free_text.GET],
    )

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=[free_text],
        search_get_request_model=search_get_model,
        search_post_request_model=search_post_model,
        collections_get_request_model=free_text.GET,
        items_get_request_model=items_get_model,
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        conforms = response_dict["conformsTo"]
        assert FreeTextConformanceClasses.SEARCH in conforms
        assert FreeTextConformanceClasses.ITEMS in conforms
        assert FreeTextConformanceClasses.COLLECTIONS in conforms

        # /search - GET, no free-text
        response = client.get(
            "/search",
            params={"collections": ["test"]},
        )
        assert response.is_success
        assert not response.text

        # /search - GET, free-text option
        response = client.get(
            "/search",
            params={
                "collections": ["test"],
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == ["ocean", "coast"]

        # /collections - GET, free-text option
        response = client.get(
            "/collections",
            params={
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == ["ocean", "coast"]

        # /items - GET, free-text option
        response = client.get(
            "/collections/test/items",
            params={
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == ["ocean", "coast"]


def test_search_free_text_search_advanced():
    """Test search endpoints with free-text ext."""
    settings = ApiSettings()
    extensions = [
        FreeTextAdvancedExtension(
            conformance_classes=[FreeTextConformanceClasses.SEARCH_ADVANCED]
        )
    ]

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=extensions,
        search_get_request_model=create_get_request_model(extensions),
        search_post_request_model=create_post_request_model(extensions),
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()

        conforms = response_dict["conformsTo"]
        assert FreeTextConformanceClasses.SEARCH_ADVANCED in conforms

        # /search - GET, no free-text
        response = client.get(
            "/search",
            params={"collections": ["test"]},
        )
        assert response.is_success
        assert not response.text

        # /search - GET, free-text option
        response = client.get(
            "/search",
            params={
                "collections": ["test"],
                "q": "+ocean,-coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == "+ocean,-coast"

        # /search - POST, no free-text
        response = client.post(
            "/search",
            json={
                "collections": ["test"],
            },
        )
        assert response.is_success
        assert not response.text

        # /search - POST, free-text option
        response = client.post(
            "/search",
            json={
                "collections": ["test"],
                "q": "+ocean,-coast",
            },
        )

        assert response.is_success, response.text
        assert response.json() == "+ocean,-coast"


def test_search_free_text_advanced_complete():
    """Test search,collections,items endpoints with free-text ext."""
    settings = ApiSettings()

    free_text = FreeTextAdvancedExtension(
        conformance_classes=[
            FreeTextConformanceClasses.SEARCH_ADVANCED,
            FreeTextConformanceClasses.ITEMS_ADVANCED,
            FreeTextConformanceClasses.COLLECTIONS_ADVANCED,
        ]
    )

    search_get_model = create_get_request_model([free_text])
    search_post_model = create_post_request_model([free_text])
    items_get_model = create_request_model(
        "ItemCollectionURI",
        base_model=ItemCollectionUri,
        mixins=[free_text.GET],
    )

    api = StacApi(
        settings=settings,
        client=DummyCoreClient(),
        extensions=[free_text],
        search_get_request_model=search_get_model,
        search_post_request_model=search_post_model,
        collections_get_request_model=free_text.GET,
        items_get_request_model=items_get_model,
    )
    with TestClient(api.app) as client:
        response = client.get("/conformance")
        assert response.is_success, response.json()
        response_dict = response.json()
        conforms = response_dict["conformsTo"]
        assert FreeTextConformanceClasses.SEARCH_ADVANCED in conforms
        assert FreeTextConformanceClasses.ITEMS_ADVANCED in conforms
        assert FreeTextConformanceClasses.COLLECTIONS_ADVANCED in conforms

        # /search - GET, no free-text
        response = client.get(
            "/search",
            params={"collections": ["test"]},
        )
        assert response.is_success
        assert not response.text

        # /search - GET, free-text option
        response = client.get(
            "/search",
            params={
                "collections": ["test"],
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == "ocean,coast"

        # /collections - GET, free-text option
        response = client.get(
            "/collections",
            params={
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == "ocean,coast"

        # /items - GET, free-text option
        response = client.get(
            "/collections/test/items",
            params={
                "q": "ocean,coast",
            },
        )
        assert response.is_success, response.text
        assert response.json() == "ocean,coast"

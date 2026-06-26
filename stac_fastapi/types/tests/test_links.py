"""Tests for link resolution functionality."""

from stac_fastapi.types.links import resolve_links


def test_resolve_links_with_absolute_and_relative_urls():
    """Test that resolve_links correctly handles a mix of absolute and relative URLs.

    This test ensures that the v6.3.1 regression is fixed: absolute URLs in STAC items
    should not be mangled by prepending the proxy path and base_url.
    """
    base_url = "http://api.stac.io/api/v1/"

    incoming_links = [
        {
            "rel": "child",
            "href": "/collections/sentinel-2",
            "type": "application/geo+json",
        },
        {
            "rel": "license",
            "href": "https://example.com/license.pdf",
            "type": "application/pdf",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)

    # 1. Check the relative link (Should have the proxy path APPLIED and PRESERVED)
    child_link = next(link for link in resolved if link["rel"] == "child")
    assert child_link["href"] == "http://api.stac.io/api/v1/collections/sentinel-2"

    # 2. Check the absolute link (Should be completely untouched)
    license_link = next(link for link in resolved if link["rel"] == "license")
    assert license_link["href"] == "https://example.com/license.pdf"

    # 3. Ensure no double-protocol mangling occurred
    assert "http://api.stac.io/api/v1/https://" not in license_link["href"]


def test_resolve_links_preserves_http_urls():
    """Test that HTTP (not HTTPS) absolute URLs are also preserved."""
    base_url = "https://api.stac.io/v1/"

    incoming_links = [
        {
            "rel": "alternate",
            "href": "http://example.com/data",
            "type": "application/json",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)
    assert resolved[0]["href"] == "http://example.com/data"


def test_resolve_links_handles_relative_urls_without_leading_slash():
    """Test that relative URLs without leading slashes are properly resolved."""
    base_url = "http://api.stac.io/api/v1/"

    incoming_links = [
        {
            "rel": "documentation",
            "href": "docs/readme.md",
            "type": "text/markdown",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)
    assert resolved[0]["href"] == "http://api.stac.io/api/v1/docs/readme.md"


def test_resolve_links_with_proxy_path():
    """Test that proxy paths are correctly applied to relative URLs."""
    base_url = "http://api.stac.io/stac/v1/"

    incoming_links = [
        {
            "rel": "child",
            "href": "/catalogs/sentinel",
            "type": "application/json",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)
    # The proxy path (/stac/v1) should be successfully retained
    assert resolved[0]["href"] == "http://api.stac.io/stac/v1/catalogs/sentinel"


def test_resolve_links_filters_inferred_links():
    """Test that inferred links (self, item, parent, etc.) are filtered out."""
    base_url = "http://api.stac.io/v1/"

    incoming_links = [
        {
            "rel": "self",
            "href": "/collections/sentinel-2",
            "type": "application/json",
        },
        {
            "rel": "custom",
            "href": "https://example.com/custom",
            "type": "application/json",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)

    # Only the custom link should be in the result
    assert len(resolved) == 1
    assert resolved[0]["rel"] == "custom"


def test_resolve_links_empty_href():
    """Test that links with missing or empty href are handled gracefully."""
    base_url = "http://api.stac.io/v1/"

    incoming_links = [
        {
            "rel": "custom",
            "href": "",
            "type": "application/json",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)

    # Should handle empty href without crashing
    assert len(resolved) == 1
    assert resolved[0]["href"] == "http://api.stac.io/v1/"


def test_resolve_links_missing_href():
    """Test that links with missing href key are handled gracefully."""
    base_url = "http://api.stac.io/v1/"

    incoming_links = [
        {
            "rel": "custom",
            "type": "application/json",
        },
    ]

    resolved = resolve_links(incoming_links, base_url)

    # Should handle missing href without crashing, defaulting to base_url
    assert len(resolved) == 1
    assert resolved[0]["href"] == "http://api.stac.io/v1/"

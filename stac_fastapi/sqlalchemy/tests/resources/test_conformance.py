def test_landing_page(app_client):
    """Test landing page"""
    resp = app_client.get("/")
    assert resp.status_code == 200
    resp_json = resp.json()

    # Make sure OpenAPI docs are linked
    docs = next(filter(lambda link: link["rel"] == "docs", resp_json["links"]))["href"]
    resp = app_client.get(docs)
    assert resp.status_code == 200

    # Make sure conformance classes are linked
    conf = next(filter(lambda link: link["rel"] == "conformance", resp_json["links"]))[
        "href"
    ]
    resp = app_client.get(conf)
    assert resp.status_code == 200

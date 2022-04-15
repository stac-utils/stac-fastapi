async def test_ping_no_param(app_client):
    """
    Test ping endpoint with a mocked client.
    Args:
        app_client (TestClient): mocked client fixture
    """
    res = await app_client.get("/_mgmt/ping")
    assert res.status_code == 200
    assert res.json() == {"message": "PONG"}

import json
import pytest


endpoints = ["endpoint1", "endpoint2"]

post_endpoints_without_data = ["endpoint1", "endpoint2", "endpoint3"]


@pytest.mark.parametrize("endpoint", endpoints)
def test_endpoints_encoding(client, endpoint):
    response = client.do_get(endpoint)
    assert response.status_code == 200
    assert isinstance(response.text, str)


@pytest.mark.parametrize("endpoint", endpoints)
def test_endpoints_content_type(client, endpoint):
    response = client.do_get(endpoint)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"


@pytest.mark.parametrize("endpoint", post_endpoints_without_data)
@pytest.mark.usefixtures("client")
def test_post_without_data(client, endpoint):
    """Test post method for endpoints which don't require data
    """
    if endpoint == "endpoint3":
        d = {"action": "did_something", "arguments_for_action": []}
        client.do_post(endpoint, data=json.dumps(d))
    r = client.do_post(endpoint)
    assert r.status_code == 200
    assert r.headers['Content-type'] == "application/json"

import pytest
import requests

urls = ["https://ya.ru", "https://google.com", "https://mail.ru"]
headers = [{"Content-type": "application/json"}, {"Content-type": "text/html"}, {}]
pairs = [(url, header) for url in urls for header in headers]


@pytest.fixture(params=pairs)
def response(request):
    print(request.param[0])
    print(request.param[1])
    return requests.get(request.param[0], headers=request.param[1])


@pytest.mark.usefixtures("response")
def test_urls(response):
    assert response.status_code == 200




import json
import pytest
import requests


class APIClient:
    headers = {"Some_Header": "shalala"}

    def __init__(self, address='https://ya.ru'):
        self.address = address

    def do_get(self, endpoint, verify_ssl=False):
        url = "/".join([self.address, endpoint])
        return requests.get(url, headers=self.headers,
                            verify=verify_ssl)

    def do_post(self, endpoint, data=None, verify_ssl=False):
        url = "/".join([self.address, endpoint])
        headers = self.headers
        headers["Content-type"] = "application/json"
        return requests.post(url, data, headers=headers, verify=verify_ssl)


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://localhost:7070")


@pytest.fixture
def client(request):
    return APIClient(request.config.getoption("--address"))

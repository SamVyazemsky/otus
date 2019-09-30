import platform
import pytest


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.122.244/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    linux_dist = platform.linux_distribution()
    return os_platform, linux_dist



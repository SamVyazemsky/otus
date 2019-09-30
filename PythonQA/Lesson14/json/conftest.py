import platform
import pytest


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.122.244/", help="Opencart web address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def extra_json_environment(request, environment_info):
    request.config._json_environment.append(("dist", environment_info[1]))
    request.config._json_environment.append(("errrrrr", environment_info[0]))

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        # only add this during call instead of during any stage
        report.test_metadata = 'whatever'
        # edit stage metadata
        report.stage_metadata = {
            'foo': 'bar'
        }
    elif report.when == 'setup':
        report.stage_metadata = {
            'hoof': 'doof'
        }
    elif report.when == 'teardown':
        report.stage_metadata = {
            'herp': 'derp'
        }


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    linux_dist = platform.linux_distribution()
    return os_platform, linux_dist


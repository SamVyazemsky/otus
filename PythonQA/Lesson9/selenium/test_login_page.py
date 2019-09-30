import pytest
import time

from Lesson6.selenium.models.page_objects.page_objects import LoginPage


@pytest.fixture(scope="session")
def open_login_page(driver, request):
    url = 'opencart/admin/'
    return driver.get("".join([request.config.getoption("--address"), url]))


@pytest.fixture(scope="module")
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture(scope="function")
def login(login_page):
    login_page.set_username("admin")
    login_page.set_password("admin")
    login_page.login()
    time.sleep(10)


@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("open_login_page")
class TestLoginPage:

    @pytest.mark.usefixtures("login")
    def test_login(self, driver):
        print(driver.current_url)
        assert "dashboard" in driver.current_url

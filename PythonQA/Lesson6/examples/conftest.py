import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver(request):
    # wd = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    capabilities = DesiredCapabilities.INTERNETEXPLORER

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    wd = webdriver.Chrome(options=options)
    # wd = webdriver.Ie(ie_options=options, capabilities={"unexpectedAlertBehaviour": "dismiss"})
    # wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://otus.ru/")
    assert driver.title == "OTUS - Онлайн-образование"

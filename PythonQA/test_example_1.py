import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions

@pytest.fixture
def chrome_browser(request):
    options = ChromeOptions()
    options.add_argument("--start-fullscreen")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example(chrome_browser):
    """
    First test
    """
    chrome_browser.get("https://otus.ru/")
    assert chrome_browser.find_element_by_class_name('header2-menu__phone').text == '+7 499 959-43-99'

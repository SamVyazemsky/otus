import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example(chrome_browser):
    """
    Example with ChromeOptions
    """
    chrome_browser.get("https://otus.ru/")
import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(chrome_browser):

    chrome_browser.get('https://www.searchengines.ru/search-console-fix.html')
    print(chrome_browser.log_types)
    for l in chrome_browser.get_log("browser"):
        print(l)


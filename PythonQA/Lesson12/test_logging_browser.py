import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option('w3c', False)
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(chrome_browser):

    chrome_browser.get('https://www.searchengines.ru/search-console-fix.html')
    print(chrome_browser.log_types)
    for l in chrome_browser.get_log("browser"):
        print(l)


import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def chrome_browser(request):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}
    wd = webdriver.Chrome(desired_capabilities=d)
    request.addfinalizer(wd.quit)
    return wd


def test_logging_browser(chrome_browser):

    chrome_browser.get('https://otus.ru/')
    print(chrome_browser.log_types)
    lst = chrome_browser.get_log("performance")
    for l in lst:
        print(l)








    time_to_load = lst[-1].get('timestamp') - lst[0].get('timestamp')

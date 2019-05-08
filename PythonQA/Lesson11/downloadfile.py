import os
import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    # options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options, desired_capabilities={"unexpectedAlertBehaviour": "dismiss"})
    request.addfinalizer(wd.quit)
    return wd


def test_download(chrome_browser):
    chrome_browser.get('https://radikal.ru/')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '1.JPG')
    input_manager = chrome_browser.find_element_by_css_selector('input.upload1')
    input_manager.send_keys(filename)

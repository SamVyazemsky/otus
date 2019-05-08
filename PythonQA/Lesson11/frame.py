import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    # options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_dnd(chrome_browser):
    chrome_browser.get("http://jqueryui.com/draggable/#scroll")
    # chrome_browser.find_element_by_link_text("/resources/demos/draggable/scroll.html")
    chrome_browser.switch_to.frame(0)

    source1 = chrome_browser.find_element_by_id('draggable')
    source2 = chrome_browser.find_element_by_id('draggable2')
    action = ActionChains(chrome_browser)

    # move element by x,y coordinates on the screen
    action.drag_and_drop(source1, source2).perform()

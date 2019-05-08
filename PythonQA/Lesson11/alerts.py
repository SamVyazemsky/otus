import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    # options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example(chrome_browser):
    chrome_browser.get("https://otus.ru/")
    chrome_browser.execute_script("alert( '123')")
    alert = chrome_browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)
    alert.accept()

    chrome_browser.execute_script("prompt('write + if you see it')", "-")
    prompt = chrome_browser.switch_to_alert()
    prompt.send_keys('+')
    prompt.accept()

    chrome_browser.execute_script('confirm("Are You Ok?")')
    confirm = chrome_browser.switch_to_alert()
    print(confirm.get_text())
    confirm.accept()

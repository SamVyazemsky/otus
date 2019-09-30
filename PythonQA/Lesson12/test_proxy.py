from browsermobproxy import Server,  Client
import pytest
import urllib.parse
from selenium import webdriver


server = Server(r"C:\Tools\browsermob-proxy-2.1.4\bin\browsermob-proxy")
server.start()
client = Client("localhost:8080")
client.port
# proxy = server.create_proxy()
client.new_har()


@pytest.fixture
def chrome_browser(request):

    chrome_options = webdriver.ChromeOptions()
    url = vurllib.parse.urlparse(client.proxy).path
    chrome_options.add_argument('--proxy-server=%s' % url)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    request.addfinalizer(driver.quit)
    return driver


def test_proxy(chrome_browser):
    # print(chrome_browser)
    # driver = chrome_browser['driver']
    chrome_browser.get('https://otus.ru/')
    print(' ')
    print(client.har)

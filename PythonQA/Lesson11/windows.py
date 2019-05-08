import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def chrome_browser(request):
    options = webdriver.ChromeOptions()
    # options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def there_is_window_other_than(windows):
    """

    :param windows:
    :return:
    """
    pass


def test_windows(chrome_browser):

    chrome_browser.get("https://otus.ru/")
    # chrome_browser.execute_script('window.open()')
    main_window = chrome_browser.current_window_handle
    old_windows = chrome_browser.window_handles
    chrome_browser.execute_script('window.open()')  # открывает новое окно
    # ожидание появления нового окна,
    # идентификатор которого отсутствует в списке oldWindows,
    # остаётся в качестве самостоятельного упражнения
    # wait = WebDriverWait
    # new_window = wait.until(there_is_window_other_than(old_windows))
    # chrome_browser.switch_to_window(new_window)
    new_window = chrome_browser.current_window_handle
    chrome_browser.switch_to_window(main_window)
    chrome_browser.close()
    all_windows = chrome_browser.window_handles
    chrome_browser.switch_to_window(all_windows[0])
    chrome_browser.close()

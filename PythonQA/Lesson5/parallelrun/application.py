from selenium import webdriver


class Application:
    def __init__(self, browser_name):
        self.browser = browser_name
        if self.browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            self.wd = webdriver.Firefox()

    def test_smth(self):
        self.wd.get("https://otus.ru/")


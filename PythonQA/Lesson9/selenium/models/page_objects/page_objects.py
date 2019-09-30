from Lesson6.selenium.models.page import BasePage
from Lesson6.selenium.models.locator import BaseLocators, LoginPageLocators


class LoginPage(BasePage):

    def __set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def __set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def __login(self):
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def login_on_page(self, username, password):
        self.__set_username(username)
        self.__set_password(password)
        self.__login()

    def __clear_password(self):
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

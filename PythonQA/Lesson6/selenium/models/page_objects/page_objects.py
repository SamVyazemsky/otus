from Lesson6.selenium.models.page import BasePage
from Lesson6.selenium.models.locator import BaseLocators, LoginPageLocators


class LoginPage(BasePage):

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element(*BaseLocators.PRIMARY_BUTTON).click()

    def clear_password(self):
        self._clear_element_(self.driver.find_element(*LoginPageLocators.PASSWORD))

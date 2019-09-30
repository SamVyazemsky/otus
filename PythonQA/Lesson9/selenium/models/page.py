import logging


from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException


logger = logging.getLogger(__name__)


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def _get_all_attributes_(self, element):
        return self.driver.execute_script(
            'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index)'
            ' { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
            element)

    def _set_element_(self, element, value):
        pass

    def _get_attribute_(self, element, attribute):
        return element.get_attribute(attribute)

    def _find_and_clear_element_(self, by, value):
        element = self.driver.find_element(by, value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def _clear_element_(self, element):
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

    def _wait_element_(self, by, value, delay=25):
        try:
            element = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            # element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def _wait_element_in_other_element_(self, element, by, value, delay=25):
        try:
            WebDriverWait(element, delay).until(EC.presence_of_element_located((by, value)))
            el = element.find_element(by, value)
            return el
        except TimeoutException:
            return False

    def _wait_and_switch(self, driver):
        try:
            # wait
            element = WebDriverWait(driver=driver, timeout=10).until(
                EC.presence_of_element_located((By.ID, 'date_views')))
            # switch
            driver.switch_to.window(driver.current_window_handle)
        except:
            logger.error('timeout but ajax until not completed')

    def _element_presented_(self, element, by, value):
        if len(element.find_element(by, value)) > 0:
            return True
        return False

    def __wait(self, timeout=15):
        """Helper method to instantiate a WebDriverWait"""
        return WebDriverWait(driver=self.driver, timeout=timeout)

    def _alert_dismiss(self):
        """
        ??alert??
        :return: ??alert????
        """
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.dismiss()
        logger.info('??alert??')
        return alert_text

    def _is_element_visible(self, *locator):
        try:
            return self._get_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def _is_element_displayed(self, element):
        if element is None:
            return False
        try:
            if isinstance(element, webelement.WebElement):
                return element.is_displayed()
            else:
                return element.src_elem.is_displayed()
        except (ElementNotVisibleException, StaleElementReferenceException):
            return False

    def _is_text_visible(self, element, text, strict=True):
        if not hasattr(element, 'text'):
            return False
        if strict:
            return element.text == text
        else:
            return text in element.text

    def _get_element_id(self, *locator):
        try:
            return self.driver.find_element(*locator).id
        except (NoSuchElementException, ElementNotVisibleException):
            return None

    def _get_element(self, *locator):
        return self.driver.find_element(*locator)

    def _get_elements(self, *locator):
        return self.driver.find_elements(*locator)

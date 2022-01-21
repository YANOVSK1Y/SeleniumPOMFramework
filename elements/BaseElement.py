from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from utils.Logger import Logger
from utils.SettingsManager import SettingsManager
from utils.Driver import Driver


class BaseElement:

    def __init__(self, locator):
        self._locator = locator

    def is_clickable(self):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(EC.element_to_be_clickable(self._locator))
        Logger.info('checking the clickability of element')
        return bool(element)

    def is_exist(self):
        Logger.info('checking existence of element')
        return bool(Driver().get_driver().find_elements_by_xpath(self._locator[1]))

    def send_keys(self, item):
        WebDriverWait(Driver().get_driver(), SettingsManager().get_value("wait_time")).until(
            EC.visibility_of_element_located(self._locator)).send_keys(item)
        Logger.info('sending some keys to element')

    def is_displayed(self):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(
            EC.visibility_of_element_located(self._locator))
        Logger.info('checking the displayability of an element')
        return bool(element)

    def click(self):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(EC.element_to_be_clickable(self._locator))
        element.click()
        Logger.info('do click on element')
        return element

    def get_text(self):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(
            EC.visibility_of_element_located(self._locator))
        Logger.info('get text from element')
        return element.text

    def get_attribute(self, attribute_name):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(
            EC.visibility_of_element_located(self._locator))
        Logger.info('get element attribute')
        return element.get_attribute(f"{attribute_name}")

    def scroll_into(self):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(
            EC.visibility_of_element_located(self._locator))
        actions = ActionChains(Driver().get_driver())
        actions.move_to_element(element).perform()
        Logger.info('scroll to element')

    def is_invisibility(self):
        element = WebDriverWait(Driver().get_driver(),
                                SettingsManager().get_value("wait_time")
                                ).until(
            EC.invisibility_of_element_located(self._locator))
        return bool(element)

    def hover_on(self):
        action = ActionChains(Driver().get_driver())
        action.move_to_element(
            WebDriverWait(Driver().get_driver(),
                          SettingsManager().get_value('wait_time')).until(
                EC.visibility_of_element_located(self._locator))).perform()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.Logger import Logger
from utils.SettingsManager import SettingsManager
from utils.Driver import Driver


class BaseForm:

    def wait_for_page_loading(self, unique_element_locator):
        return WebDriverWait(Driver().get_driver(), SettingsManager().get_value("wait_time")
                             ).until(
            EC.presence_of_element_located(unique_element_locator))

    def check_existence_of_page_by_element(self, element):
        Logger.info('check existence of page by element')
        return bool(element.is_displayed())

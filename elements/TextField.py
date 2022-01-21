from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.SettingsManager import SettingsManager
from utils.Driver import Driver
from utils.Logger import Logger
from elements.BaseElement import BaseElement


class TextField(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)

    def send_keys(self, item):
        WebDriverWait(Driver().get_driver(), SettingsManager().get_value("wait_time")).until(
            EC.visibility_of_element_located(self._locator)).send_keys(item)
        Logger.info('send some keys to element')
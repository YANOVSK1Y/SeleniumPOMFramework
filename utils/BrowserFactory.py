from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOp

from selenium.webdriver.firefox.options import Options as FirefoxOp
from webdriver_manager.firefox import GeckoDriverManager

from utils.SettingsManager import SettingsManager
from utils.Logger import Logger

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class BrowserFactory:

    def __init__(self):

        if SettingsManager().get_value("browser").lower() == "chrome":
            chrome_options = ChromeOp()
            chrome_options.add_argument(
                f"--lang={SettingsManager().get_value('language').lower()}")
            chrome_options.add_argument(
                f"--window-size={SettingsManager().get_value('window_width')},"
                f"{SettingsManager().get_value('window_height')}",
            )
            if SettingsManager().get_value("incognito") == "true":
                chrome_options.add_argument("--incognito")

            caps = DesiredCapabilities().CHROME
            caps["pageLoadStrategy"] = "none"

            self._web_driver = webdriver.Chrome(ChromeDriverManager().install(),
                                                desired_capabilities=caps,
                                                chrome_options=chrome_options)
            Logger.info('Created Chrome driver')

        elif SettingsManager().get_value("browser").lower() == "firefox":
            firefox_options = FirefoxOp()
            firefox_options.add_argument(
                f"--lang={SettingsManager().get_value('language').lower()}")
            firefox_options.add_argument(
                f"--window-size={SettingsManager().get_value('window_width')},"
                f"{SettingsManager().get_value('window_height')}")
            self._web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                                 options=firefox_options)
            Logger.info('Created FireFox driver')
        else:
            raise KeyError

    def set_up(self):
        return self._web_driver

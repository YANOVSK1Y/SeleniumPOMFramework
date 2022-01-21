
from utils.SingleTon import SingletonType
from utils.BrowserFactory import BrowserFactory
from utils.Logger import Logger


class Driver(object, metaclass=SingletonType):

    def __init__(self):
        self._web_driver = BrowserFactory().set_up()
        Logger.info('Choose and setup web driver success')

    def get_driver(self):
        return self._web_driver

    def close(self):
        self._web_driver.close()

    def quit(self):
        self._web_driver.quit()

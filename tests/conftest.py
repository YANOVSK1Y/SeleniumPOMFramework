import pytest
from utils.Logger import Logger
from utils.Driver import Driver


@pytest.fixture(scope='function')
def setup(request):
    driver = Driver().get_driver()
    Logger.info('Initialize Driver')
    yield
    driver.quit()
    Logger.info('Driver Quit')
    Driver.clear()
    Logger.info('Driver Cleared')


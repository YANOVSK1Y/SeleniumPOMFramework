import pytest
from forms.HomePage import HomePage
from forms.AboutPage import AboutPage
from forms.StorePage import StorePage
from utils.SettingsManager import SettingsManager
from utils.Driver import Driver
from utils.Logger import Logger


@pytest.mark.usefixtures("setup")
class TestHomeAboutStorePages:

    def test_go_home_about_store_pages(self):

        Logger.info(">>>Starting test case 1<<<")
        self.homePage = HomePage()
        Logger.info("Initialise home page instance")
        self.aboutPage = AboutPage()
        Logger.info("Initialise about page instance")
        self.storePage = StorePage()
        Logger.info("Initialise store page instance")

        Logger.info("Step 1:")
        Driver().get_driver().get(SettingsManager().get_value("url"))
        Logger.info("Open steam main page")

        assert self.homePage.check_page_existence(), 'home page is not exist'
        Logger.info("Check home page existence success")

        Logger.info("Step 2:")
        self.homePage.click_about_page_button()
        Logger.info("Open about page")
        assert self.aboutPage.check_page_existence(), 'About page is not exist'
        Logger.info("Check about page existence success")

        Logger.info("Step 3:")
        Logger.info("Get players online value")
        players_online_value = self.aboutPage.get_players_online_value()
        assert players_online_value, 'Can\'t get players online value'
        Logger.info("Players online value received")

        Logger.info("Get players playing now value")
        players_playing_now_value = self.aboutPage.get_players_playing_now_value()
        assert players_playing_now_value, 'Can\'t get players playing now value'
        Logger.info("Players playing now value received")

        Logger.info("Compare players status values")
        assert players_online_value > players_playing_now_value, \
            'Can\'t compere players values'
        Logger.info("Check players stats success. "
                                   "Playing now players are less than players online")

        Logger.info("Open store page")
        self.aboutPage.click_store_page_button()

        assert self.storePage.check_page_existence(), 'Store page is not exist'
        Logger.info("Check store page existence success")

        Logger.info(">>>END test case 1<<<")

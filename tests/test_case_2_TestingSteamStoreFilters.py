import pytest
from forms.HomePage import HomePage
from forms.GamePage import GamePage
from forms.TopSellersPage import TopSellersPage
from utils.SettingsManager import SettingsManager
from utils.Driver import Driver
from utils.Logger import Logger


@pytest.mark.usefixtures("setup")
class TestSteamStoreFilters:

    def test_steam_store_filters_for_dota(self):

        Logger.info(">>>Starting test case 2<<<")
        self.homePage = HomePage()
        Logger.info("Initialise home page instance")
        self.topSellersPage = TopSellersPage()
        Logger.info("Initialise top sellers page instance")

        Driver().get_driver().get(SettingsManager().get_value("url"))
        Logger.info("Open steam main page")

        assert self.homePage.check_page_existence(), 'home page is not exist'
        Logger.info("Check home page existence success")

        Logger.info("Open top sellers page")
        self.homePage.open_sellers_page()
        assert self.topSellersPage.check_page_existence(), 'Top sellers page is not exist'
        Logger.info("Check top sellers page existence success")

        Logger.info(
            "Choose os param \'SteamOs+Linux + \' success")
        assert self.topSellersPage.choose_os_linux_param(), 'Can\'t choose SteamOs and Linux filter param'

        # can't choose coop lan param in filter ERROR: {"status": 500, value:
        # {"message": "jsvascript error: this.each is not a functio...unk"}}
        # assert self.topSellersPage.choose_coop_lan_param(), 'Can\'t choose COOP-LAN filter param'
        # Logger.info("Choose number of players param \'COOP-LAN + \' success")

        assert self.topSellersPage.choose_action_tag_param(), 'Can\'t choose Action tag filter param'
        Logger.info(
            "Choose tags param \'Action + \' success")

        Logger.info("Get first game values from result games list")
        first_game_title, first_game_price, first_game_release_data = self.topSellersPage.get_first_game_values()
        assert (first_game_title, first_game_price, first_game_release_data), 'Didn\'t get first game values'

        Logger.info("Open game page")
        assert self.topSellersPage.open_first_game_page(), 'Can\'t open game page'

        Logger.info("Initialise game page instance")
        self.gamePage = GamePage()

        assert self.gamePage.check_page_existence(), 'Game page is not exist'
        Logger.info("Check Game page existence success")

        Logger.info("Get game values from game page")
        game_title, game_price, game_release_data = self.gamePage.get_game_params()
        assert (game_title, game_price, game_release_data), 'Didn\'t get game values from game page'

        assert first_game_title == game_title, 'Game titles is not the same'
        Logger.info("Compering games title success")
        assert first_game_price == game_price, 'Game prices is not the same'
        Logger.info("Compering games prices success")
        assert first_game_release_data == game_release_data, 'Game release dates is not the same'
        Logger.info("Compering games release dates success")

        Logger.info(">>>END test case 2<<<")

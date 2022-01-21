from selenium.webdriver.common.by import By
from forms.BaseForm import BaseForm
from elements.TextField import TextField
from elements.Button import Button
from utils.SteamNavBarMenuLocatorManager import SteamNavBarMenuLocatorManager


class AboutPage(BaseForm):

    UNIQUE_ITEM_LOCATOR = (By.XPATH, '//div[@class="online_stats"]')
    STORE_BTN_LOCATOR = (By.XPATH, '//div[@class="supernav_container"]//a[contains(text(), "STORE")]')

    def check_page_existence(self):
        unique_item_alert_page_tf = TextField(self.UNIQUE_ITEM_LOCATOR)
        return unique_item_alert_page_tf.is_displayed()

    def get_players_online_value(self):
        online_players = TextField(self.UNIQUE_ITEM_LOCATOR)
        online_value = online_players.get_text().split('\n')[1]
        str_without_comas = str()
        for i in online_value.split(','):
            str_without_comas += i
        return int(str_without_comas)

    def get_players_playing_now_value(self):
        playing_now_players = TextField(self.UNIQUE_ITEM_LOCATOR)
        playing_now_value = playing_now_players.get_text().split('\n')[3]
        str_without_comas = str()
        for i in playing_now_value.split(','):
            str_without_comas += i
        return int(str_without_comas)

    def click_store_page_button(self):
        store_btn = Button(SteamNavBarMenuLocatorManager.get_menu_item_locator('store'))
        store_btn.click()

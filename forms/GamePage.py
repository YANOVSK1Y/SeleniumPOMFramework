from selenium.webdriver.common.by import By

from elements.Img import Img
from forms.BaseForm import BaseForm
from elements.TextField import TextField


class GamePage(BaseForm):

    UNIQUE_ITEM_LOCATOR = (By.XPATH, '//div[contains(@class, "block_content") and contains(@class, "page_content")]')
    GAME_TITLE_LOCATOR = (By.XPATH, '//div[@id="appHubAppName"]')
    GAME_PRICE_LOCATOR = (By.XPATH, '//div[@class="game_area_purchase_game_wrapper"]//div[@class="game_area_purchase_game"]//div[@class="game_purchase_price price"]')
    GAME_DISCOUNT_PRICE_LOCATOR = (By.XPATH, '//div[@class="game_purchase_action_bg"]//div[@class="discount_final_price"]')
    GAME_RELEASE_DATA_LOCATOR = (By.XPATH, '//div[@class="release_date"]//div[@class="date"]')

    def check_page_existence(self):
        return self.check_existence_of_page_by_element(Img(self.UNIQUE_ITEM_LOCATOR))

    def get_game_params(self):
        game_title_text_field = TextField(self.GAME_TITLE_LOCATOR)
        game_price_text_field = TextField(self.GAME_PRICE_LOCATOR)
        if not game_price_text_field.is_exist():
            game_price_text_field = TextField(self.GAME_DISCOUNT_PRICE_LOCATOR)
        game_release_date_text_field = TextField(
            self.GAME_RELEASE_DATA_LOCATOR)
        return (game_title_text_field.get_text(),
                game_price_text_field.get_text(),
                game_release_date_text_field.get_text())
from selenium.webdriver.common.by import By

from forms.BaseForm import BaseForm
from elements.PopUpMenu import PopUpMenu
from elements.Button import Button
from elements.Img import Img
from utils.SteamNavBarMenuLocatorManager import SteamNavBarMenuLocatorManager


class HomePage(BaseForm):

    UNIQUE_ITEM_LOCATOR = (By.XPATH, '//img[@class="home_page_gutter_giftcard"]')
    NEW_NOTEWORTHY_MENU_ITEM_LOCATOR = (By.XPATH, '//div[@id="noteworthy_tab"]')
    TOP_SELLERS_BTN_LOCATOR = (By.XPATH, '//a[contains(@class,"popup_menu_item") and contains(text(), "Top Sellers")]')

    def check_page_existence(self):
        return self.check_existence_of_page_by_element(Img(self.UNIQUE_ITEM_LOCATOR))

    def click_about_page_button(self):
        about_btn = Button(SteamNavBarMenuLocatorManager.get_menu_item_locator('about'))
        about_btn.click()

    def open_sellers_page(self):
        new_noteworthy_btn = PopUpMenu(self.NEW_NOTEWORTHY_MENU_ITEM_LOCATOR)
        new_noteworthy_btn.hover_on()
        top_sellers_btn = Button(self.TOP_SELLERS_BTN_LOCATOR)
        top_sellers_btn.click()


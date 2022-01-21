from selenium.webdriver.common.by import By

from forms.BaseForm import BaseForm
from elements.TextField import TextField
from elements.Button import Button
from elements.PopUpMenu import PopUpMenu
from elements.Img import Img


class TopSellersPage(BaseForm):

    UNIQUE_ITEM_LOCATOR = (By.XPATH, '//h2[contains(@class, "pageheader") and contains(@class, "full")]')

    OS_PARAM_LOCATOR = (By.XPATH,'//span[@data-loc="SteamOS + Linux"]//span[@class="tab_filter_control_checkbox"]')
    OS_PARAM_CHECKED_LOCATOR = (By.XPATH, '//span[contains(@class, "tab_filter_control tab_filter_control_include") and contains(@class, "checked")]')

    COOP_lAN_HEADER_COLLAPSED_LOCATOR = (By.XPATH, '//div[contains(@class, "block search_collapse_block") and contains(@class, "collapsed") and @data-collapse-name="category3"]')
    COOP_LAN_CHECK_BOX_LOCATOR = (By.XPATH, '//div[@data-collapse-name="category3"]//div[contains(@class, "block_content_inner")]//div[@data-value="48"]')
    COOP_LAN_CHECK_BOX_CHECKED_LOCATOR = (By.XPATH, '//span[@data-param="category3" and @data-value="48" and contains(@class, "checked")]')

    TAGS_HEADER_COLLAPSED_LOCATOR = (By.XPATH, '//div[contains(@class, "block search_collapse_block") and contains(@class, "collapsed") and @data-collapse-name="tags"]')
    TAGS_MENU_ACTION_PARAM_LOCATOR = (By.XPATH, '//span[@data-param="tags" and @data-loc="Action"]')
    TAGS_ACTION_TAG_CHECKED_LOCATOR = (By.XPATH, '//div[@data-param="tags" and @data-value="19" and contains(@class, "checked")]')

    OPACITY_RESULT_LIST = (By.XPATH, '//div[@id="search_result_container" and @style="opacity: 0.5;"]')
    SEARCH_RESULT_LIST_LOADING_BAR = (By.XPATH, '//div[@id="search_results_loading"]')

    FIRST_GAME_TITLE_LOCATOR = (By.XPATH, '//div[@id="search_resultsRows"]/a[1]//span[@class="title"]')
    FIRST_GAME_RELEASE_DATA_LOCATOR = (By.XPATH, '//div[@id="search_resultsRows"]/a[1]//div[contains(@class, "col") and contains(@class, "search_released") and contains(@class, "responsive_secondrow")]')
    FIRST_GAME_PRICE_LOCATOR = (By.XPATH, '//div[@id="search_resultsRows"]/a[1]//div[@class="col search_price  responsive_secondrow"]')
    FIRST_GAME_PRICE_DISCOUNTED_LOCATOR = (By.XPATH, '//div[@id="search_resultsRows"]/a[1]//div[contains(@class, "search_price") and contains(@class, "discounted")]')

    FIRST_GAME_IN_LIST_LOCATOR = (By.XPATH, '//div[@id="search_resultsRows"]/a[1]')

    def check_page_existence(self):
        return self.check_existence_of_page_by_element(TextField(self.UNIQUE_ITEM_LOCATOR))

    def choose_os_linux_param(self):
        os_param_btn = Button(self.OS_PARAM_LOCATOR)
        os_param_btn.scroll_into()
        os_param_btn.click()
        os_param_btn_checked = Button(self.OS_PARAM_CHECKED_LOCATOR)
        return bool(os_param_btn_checked.is_exist())

    def choose_coop_lan_param(self):
        coop_lan_header_pop_up = PopUpMenu(self.COOP_lAN_HEADER_COLLAPSED_LOCATOR)
        if coop_lan_header_pop_up.is_exist():
            coop_lan_header_pop_up.scroll_into()
            coop_lan_header_pop_up.click()
        coop_lan_btn = Button(self.COOP_LAN_CHECK_BOX_LOCATOR)
        coop_lan_btn.scroll_into()
        coop_lan_btn.click()
        checked_coop_lan_checkbox = Button(self.COOP_LAN_CHECK_BOX_CHECKED_LOCATOR)
        return bool(checked_coop_lan_checkbox.is_exist())

    def choose_action_tag_param(self):
        action_tag_header_popup = PopUpMenu(self.TAGS_HEADER_COLLAPSED_LOCATOR)
        if action_tag_header_popup.is_exist():
            action_tag_header_popup.scroll_into()
            action_tag_header_popup.click()
        else:
            pass
        tag_action_btn = Button(self.TAGS_MENU_ACTION_PARAM_LOCATOR)
        tag_action_btn.click()

        result_loader_icon = Img(self.OPACITY_RESULT_LIST)
        res_load_bar = Img(self.SEARCH_RESULT_LIST_LOADING_BAR)

        return bool(result_loader_icon.is_invisibility() and res_load_bar.is_invisibility())

    def get_first_game_values(self):
        game_title_text_field = TextField(self.FIRST_GAME_TITLE_LOCATOR)
        game_price_text_field = TextField(self.FIRST_GAME_PRICE_LOCATOR)
        game_release_date_text_field = TextField(self.FIRST_GAME_RELEASE_DATA_LOCATOR)
        if not game_price_text_field.is_exist():
            game_price_text_field = TextField(self.FIRST_GAME_PRICE_DISCOUNTED_LOCATOR)
            game_price = game_price_text_field.get_text().split('\n')[1]
        else:
            game_price = game_price_text_field.get_text()
        return (game_title_text_field.get_text(),
                game_price,
                game_release_date_text_field.get_text())

    def open_first_game_page(self):
        first_game_btn = Button(self.FIRST_GAME_IN_LIST_LOCATOR)
        return bool(first_game_btn.click())

from selenium.webdriver.common.by import By


class SteamNavBarMenuLocatorManager:

    @staticmethod
    def get_menu_item_locator(item_name):
        return (By.XPATH,
                f'//div[@class="supernav_container"]//a[contains(text(), "{item_name.upper()}")]')

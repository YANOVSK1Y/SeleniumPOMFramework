from selenium.webdriver.common.by import By
from forms.BaseForm import BaseForm
from elements.Img import Img


class StorePage(BaseForm):

    UNIQUE_ITEM_LOCATOR = (By.XPATH, '//img[@class="home_page_gutter_giftcard"]')

    def check_page_existence(self):
        return self.check_existence_of_page_by_element(Img(self.UNIQUE_ITEM_LOCATOR))
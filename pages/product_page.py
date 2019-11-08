from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.verify_message_added_product_name_to_basket()
        self.verify_message_product_price_to_basket()

    def should_be_add_to_basket_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADDBASKET_BUTTON), "addBasket button isn't presented"

    def verify_message_added_product_name_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "ProductName button isn't presented"

    def verify_message_product_price_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "ProductPrice button isn't presented"

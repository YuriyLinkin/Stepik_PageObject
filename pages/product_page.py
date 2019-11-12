from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.ADDBASKET_BUTTON).click()


    def verify_message_added_product_name_to_basket(self):

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_FOR_PRODUCT)
        assert product_name == message.text, "Book wasn't added to cart"



    def verify_message_product_price_to_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_WITH_PRICE)
        assert product_price == message.text, "Incorrect product price in cart"

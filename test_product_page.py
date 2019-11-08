from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.should_be_add_to_basket_button()    # verify AddToBasket button is exist on current page
    browser.ADDBASKET_BUTTON.click()

    product_page.should_be_add_to_basket_button()
    product_page.verify_message_added_product_name_to_basket()
    product_page.verify_message_product_price_to_basket()

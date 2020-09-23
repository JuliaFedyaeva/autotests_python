from selenium import webdriver
import locators as _locators
import utils


def add_product_to_cart():
    # Data
    success_add_message_locator = 'div.alertinner'
    success_message = 'был добавлен в вашу корзину'
    item_in_cart_locator = 'div.alertinner strong'
    item_in_cart_name = 'h3 a'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        utils.find(browser, _locators.catalog_link).click()

        page_catalog_detector = utils.find(browser, _locators.catalog_heading_locator).text
        assert _locators.catalog_heading in page_catalog_detector, \
            "Search heading '%s' should contain text '%s'" % (page_catalog_detector, _locators.catalog_heading)

        # Steps
        utils.click_add_to_cart(browser)

        success_add_message = utils.find(browser, success_add_message_locator).text
        assert success_message in success_add_message, \
            "Search heading '%s' should contain text '%s'" % (success_add_message, success_message)

        what_is_in_cart = utils.find(browser, item_in_cart_locator).text

        utils.view_cart(browser)

        cart = utils.find(browser, item_in_cart_name).text

        # Assert
        assert what_is_in_cart == cart, "Wrong item in the cart"

    finally:
        browser.quit()


add_product_to_cart()

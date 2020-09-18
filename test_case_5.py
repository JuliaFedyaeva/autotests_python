from selenium import webdriver
import locators as _locators


def add_product_to_cart():
    # Data
    catalog_heading = 'Все товары'
    catalog_heading_locator = 'div.page-header.action h1'
    success_add_message_locator = 'div.alertinner'
    success_message = 'был добавлен в вашу корзину'
    item_in_cart_locator = 'div.alertinner strong'
    item_in_cart_name = 'h3 a'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        browser.find_element_by_xpath(_locators.catalog_link).click()

        page_catalog_detector = browser.find_element_by_css_selector(catalog_heading_locator).text
        assert catalog_heading in page_catalog_detector, \
            "Search heading '%s' should contain text '%s'" % (page_catalog_detector, catalog_heading)

        # Steps
        browser.find_element_by_xpath(_locators.button_add_to_cart).click()

        success_add_message = browser.find_element_by_css_selector(success_add_message_locator).text
        assert success_message in success_add_message, \
            "Search heading '%s' should contain text '%s'" % (success_add_message, success_message)

        what_is_in_cart = browser.find_element_by_css_selector(item_in_cart_locator).text

        browser.find_element_by_css_selector(_locators.button_view_cart).click()

        cart = browser.find_element_by_css_selector(item_in_cart_name).text

        # Assert
        assert what_is_in_cart == cart

    finally:
        browser.quit()


add_product_to_cart()

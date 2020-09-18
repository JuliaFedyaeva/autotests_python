from selenium import webdriver
from selenium.webdriver.support.ui import Select
import locators as _locators
import test_case_3
import test_case_5


def payment_without_card():
    # Data
    name = 'Max'
    lastname = 'Payne'
    address = 'PlayStation'
    city = 'Nowhere'
    postcode = '652877'
    page_shipping_heading = 'Адрес доставки'
    heading_shipping_locator = 'div.sub-header h1'
    country_locator = 'select#id_country'
    russia = 'RU'
    heading_payment_locator = 'div.sub-header h1'
    page_payment_heading = 'Введите параметры платежа'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        test_case_3.authorization()
        test_case_5.add_product_to_cart()

        # Steps
        browser.find_element_by_css_selector(_locators.button_to_order).click()

        page_shipping_detector = browser.find_element_by_css_selector(heading_shipping_locator).text
        assert page_shipping_heading in page_shipping_detector, \
            "Search heading '%s' should contain text '%s'" % (page_shipping_detector, heading_shipping_locator)

        browser.find_element_by_css_selector(_locators.input_name).send_keys(name)
        browser.find_element_by_css_selector(_locators.input_lastname).send_keys(lastname)
        browser.find_element_by_css_selector(_locators.input_address).send_keys(address)
        browser.find_element_by_css_selector(_locators.input_city).send_keys(city)
        browser.find_element_by_css_selector(_locators.input_postcode).send_keys(postcode)

        select = Select(browser.find_element_by_id(country_locator))
        select.select_by_value(russia)

        button_to_next_step = browser.find_element_by_css_selector(_locators.link_to_payment).click()

        # тут по идее должна быть проверка способа доставки, но нет такого раздела почему-то,
        # сразу перекидывает на шаг оплаты

        page_payment_detector = browser.find_element_by_css_selector(heading_payment_locator).text
        assert page_payment_heading in page_payment_detector

        # здесь поля оплаты остаются пустыми

        # Assert
        button_disabled = button_to_next_step.getAttribute('disabled')
        assert button_disabled == "true", "No disabled button on payment page"

        button_to_next_step.click()

    finally:
        browser.quit()


payment_without_card()

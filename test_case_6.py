from selenium import webdriver
import locators as _locators
import utils
import test_data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_payment_without_card():
    # Data
    heading_shipping_locator = 'div.sub-header h1'
    country_locator = 'select#id_country'
    heading_payment_locator = 'div.sub-header h1'
    page_payment_heading = 'Введите параметры платежа'
    page_shipping_heading = 'Адрес доставки'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        utils.find(browser, _locators.login_link).click()
        utils.authorizate(browser, test_data.email, test_data.password)

        WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.XPATH, _locators.success_message_locator))
        )

        success_message_text = utils.find_xpath(browser, _locators.success_message_locator).text
        assert _locators.success_message in success_message_text, \
            "Search success message '%s' should contain text '%s'" % (success_message_text, _locators.success_message)

        WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, _locators.catalog_link))
        )

        utils.find(browser, _locators.catalog_link).click()

        page_catalog_detector = utils.find(browser, _locators.catalog_heading_locator).text
        assert _locators.catalog_heading in page_catalog_detector, \
            "Search heading '%s' should contain text '%s'" % (page_catalog_detector, _locators.catalog_heading)

        utils.click_add_to_cart(browser)

        WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, _locators.button_view_cart))
        )

        utils.view_cart(browser)

        # Steps
        utils.find(browser, _locators.button_to_order).click()

        page_shipping_detector = utils.find(browser, heading_shipping_locator).text
        assert page_shipping_heading in page_shipping_detector, \
            "Search heading '%s' should contain text '%s'" % (page_shipping_detector, heading_shipping_locator)

        WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, heading_shipping_locator))
        )

        utils.set_address(browser, test_data.name, test_data.lastname, test_data.address, test_data.city, test_data.postcode, country_locator, test_data.country)
        utils.click_next_step_order(browser)

        # тут по идее должна быть проверка способа доставки, но нет такого раздела почему-то,
        # сразу перекидывает на шаг оплаты

        WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, heading_payment_locator))
        )

        page_payment_detector = utils.find(browser, heading_payment_locator).text
        assert page_payment_heading in page_payment_detector

        # здесь поля оплаты остаются пустыми

        WebDriverWait(browser, 12).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, _locators.link_to_payment))
        )

        # Assert
        button_disabled = _locators.link_to_payment.getAttribute('disabled')
        assert button_disabled == "true", "No disabled button on payment page"

        button_disabled.click()

    finally:
        browser.quit()

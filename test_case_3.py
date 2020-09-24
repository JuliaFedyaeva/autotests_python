import locators as _locators
import test_data
import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization(browser):
    # Data
    auth_heading = 'Войти'
    page_auth_locator = 'form#login_form h2'

    # Arrange
    browser.get(_locators.main_page_link)

    utils.find(browser, _locators.login_link).click()

    page_auth_detector = utils.find(browser, page_auth_locator).text
    assert auth_heading in page_auth_detector, \
        "Search heading '%s' should contain text '%s'" % (page_auth_detector, auth_heading)

    # Steps
    utils.authorizate(browser, test_data.email, test_data.password)

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, _locators.success_message_locator))
    )

    # Assert
    success_message_text = utils.find_xpath(browser, _locators.success_message_locator).text
    assert _locators.success_message in success_message_text, \
        "Search success message '%s' should contain text '%s'" % (success_message_text, _locators.success_message)

import locators as _locators
import test_data
import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_password_remind(browser):
    # Data
    auth_heading = 'Войти'
    page_auth_locator = 'form#login_form h2'
    page_heading = 'Восстановление пароля'
    page_pswrd_reset_locator = 'div.page-header.action h1'
    success_message_locator = 'div.page-header.action h1'
    success_message = 'Письмо отправлено'

    # Arrange
    browser.get(_locators.main_page_link)
    utils.find(browser, _locators.login_link).click()

    page_auth_detector = utils.find(browser, page_auth_locator).text
    assert auth_heading in page_auth_detector, \
        "Search heading '%s' should contain text '%s'" % (page_auth_detector, auth_heading)

    # Steps
    utils.find(browser, _locators.reset_password).click()

    WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, page_pswrd_reset_locator))
    )

    page_reset_pswrd_detector = utils.find(browser, page_pswrd_reset_locator).text
    assert page_heading in page_reset_pswrd_detector, \
        "Search heading '%s' should contain text '%s'" % (page_reset_pswrd_detector, page_heading)

    utils.reset_password(browser, test_data.email)

    # Assert
    success_message_text = utils.find(browser, success_message_locator).text
    assert success_message in success_message_text, \
        "Search success message '%s' should contain text '%s'" % (success_message_text, success_message)

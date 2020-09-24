import locators as _locators
import test_data
import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration(browser):
    # Data
    page_heading_locator = 'form#register_form h2'
    page_heading = 'Зарегистрироваться'
    success_message = 'Спасибо за регистрацию!'
    success_message_locator = '//div[contains(text(), "Спасибо за регистрацию")]'

    # Arrange
    browser.get(_locators.main_page_link)

    utils.find(browser, _locators.login_link).click()
    page_detector_text = utils.find(browser, page_heading_locator).text
    assert page_heading in page_detector_text, \
        "Search page heading '%s' should contain text '%s'" % (page_detector_text, page_heading)

    # Steps
    utils.registrate(browser, test_data.new_email, test_data.password)

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, success_message_locator))
    )

    # Assert
    success_message_text = utils.find_xpath(browser, success_message_locator).text
    assert success_message in success_message_text, \
        "Search success message on page '%s'should contain text '%s'" % (success_message_text, success_message)

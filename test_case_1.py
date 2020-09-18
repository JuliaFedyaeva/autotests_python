from selenium import webdriver
import locators as _locators


def registration():
    # Data
    page_heading_locator = 'form#register_form h2'
    page_heading = 'Зарегистрироваться'
    success_message_locator = 'div.alertinner.wicon'
    success_message = 'Спасибо за регистрацию!'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        browser.find_element_by_css_selector(_locators.login_link).click()
        page_detector_text = browser.find_element_by_css_selector(page_heading_locator).text
        assert page_heading in page_detector_text, \
            "Search page heading '%s' should contain text '%s'" % (page_detector_text, page_heading)

        # Steps
        browser.find_element_by_css_selector(_locators.input_email).send_keys(_locators.new_email)
        browser.find_element_by_css_selector(_locators.input_password).send_keys(_locators.password)
        browser.find_element_by_css_selector(_locators.input_repeat_password).send_keys(_locators.password)
        browser.find_element_by_css_selector(_locators.button_reg).click()

        # Assert
        success_message_text = browser.find_element_by_css_selector(success_message_locator).text
        assert success_message in success_message_text, \
            "Search success message on page '%s'should contain text '%s'" % (success_message_text, success_message)

    finally:
        browser.quit()


registration()

from selenium import webdriver
import locators as _locators


def authorization():
    # Data
    auth_heading = 'Войти'
    page_auth_locator = 'form#login_form h2'
    success_message = 'Рады видеть вас снова'
    success_message_locator = 'div.alertinner.wicon'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        browser.find_element_by_css_selector(_locators.login_link).click()

        page_auth_detector = browser.find_element_by_css_selector(page_auth_locator).text
        assert auth_heading in page_auth_detector, \
            "Search heading '%s' should contain text '%s'" % (page_auth_detector, auth_heading)

        # Steps
        browser.find_element_by_css_selector(_locators.input_email_auth).send_keys(_locators.email)
        browser.find_element_by_css_selector(_locators.input_password_auth).send_keys(_locators.password)
        browser.find_element_by_css_selector(_locators.button_auth).click()

        # Assert
        success_message_text = browser.find_element_by_css_selector(success_message_locator).text
        assert success_message in success_message_text, \
            "Search success message '%s' should contain text '%s'" % (success_message_text, success_message)

    finally:
        browser.quit()

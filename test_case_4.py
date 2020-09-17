from selenium import webdriver
import locators as _locators


def password_remind():
    # Data
    input_remind_password = 'input#id_email'
    button_reset_password = '//button[contains(text(), "Отправить письмо для смены пароля")]'
    auth_heading = 'Войти'
    page_auth_locator = 'form#login_form h2'
    page_heading = 'Восстановление пароля'
    page_pswrd_reset_locator = 'div.page-header.action h1'
    success_message_locator = 'div.page-header.action h1'
    success_message = 'Письмо отправлено'


    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        browser.find_element_by_id(_locators.login_link).click()

        page_auth_detector = browser.find_element_by_css_selector(page_auth_locator).text
        assert auth_heading in page_auth_detector, \
            "Search heading '%s' should contain text '%s'" % (page_auth_detector, auth_heading)

        # Steps
        browser.find_element_by_css_selector(_locators.reset_password).click()

        page_reset_pswrd_detector = browser.find_element_by_css_selector(page_pswrd_reset_locator).text
        assert page_heading in page_reset_pswrd_detector, \
            "Search heading '%s' should contain text '%s'" % (page_reset_pswrd_detector, page_heading)

        browser.find_element_by_css_selector(input_remind_password).send_keys(_locators.email)
        browser.find_element_by_xpath(button_reset_password).click()

        # Assert
        success_message_text = browser.find_element_by_css_selector(success_message_locator).text
        assert success_message in success_message_text, \
            "Search success message '%s' should contain text '%s'" % (success_message_text, success_message)

    finally:
        browser.quit()

import locators as _locators

def find(parent, locator):
    return parent.find_element_by_css_selector(locator)

def find_xpath(parent, locator):
    return parent.find_element_by_xpath(locator)

def registrate(parent, new_email, password):
    parent.find_element_by_css_selector(_locators.input_email).send_keys(new_email)
    parent.find_element_by_css_selector(_locators.input_password).send_keys(password)
    parent.find_element_by_css_selector(_locators.input_repeat_password).send_keys(password)
    parent.find_element_by_css_selector(_locators.button_reg).click()

def search_item(parent, book_name):
    parent.find_element_by_css_selector(_locators.input_search).send_keys(book_name)
    parent.find_element_by_css_selector(_locators.input_search_button).click()

def authorizate(parent, email, password):
    parent.find_element_by_css_selector(_locators.input_email_auth).send_keys(email)
    parent.find_element_by_css_selector(_locators.input_password_auth).send_keys(password)
    parent.find_element_by_css_selector(_locators.button_auth).click()

def reset_password(parent, email):
    parent.find_element_by_css_selector(_locators.input_remind_password).send_keys(email)
    parent.find_element_by_xpath(_locators.button_reset_password).click()

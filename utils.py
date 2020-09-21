import locators as _locators

def find(parent, locator):
    return parent.find_element_by_css_selector(locator)

def registrate(parent, new_email, password):
    parent.find_element_by_css_selector(_locators.input_email).send_keys(new_email)
    parent.find_element_by_css_selector(_locators.input_password).send_keys(password)
    parent.find_element_by_css_selector(_locators.input_repeat_password).send_keys(password)
    parent.find_element_by_css_selector(_locators.button_reg).click()

def authorizaite(parent, book_name):
    parent.find_element_by_css_selector(_locators.input_search).send_keys(book_name)
    parent.find_element_by_css_selector(_locators.input_search_button).click()


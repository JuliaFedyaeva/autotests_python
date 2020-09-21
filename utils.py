import locators as _locators
from selenium.webdriver.support.ui import Select


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

def click_add_to_cart(parent):
    parent.find_element_by_xpath(_locators.button_add_to_cart).click()

def view_cart(parent):
    parent.find_element_by_css_selector(_locators.button_view_cart).click()

def set_address(parent, name, lastname, address, city, postcode, country_locator, country):
    parent.find_element_by_css_selector(_locators.input_name).send_keys(name)
    parent.find_element_by_css_selector(_locators.input_lastname).send_keys(lastname)
    parent.find_element_by_css_selector(_locators.input_address).send_keys(address)
    parent.find_element_by_css_selector(_locators.input_city).send_keys(city)
    parent.find_element_by_css_selector(_locators.input_postcode).send_keys(postcode)
    select = Select(parent.find_element_by_css_selector(country_locator))
    select.select_by_value(country)

def click_next_step_order(parent):
    parent.find_element_by_xpath(_locators.button_to_continue).click()

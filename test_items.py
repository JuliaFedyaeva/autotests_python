from selenium import webdriver
import utils
import locators as _locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_button_add_to_cart(browser):
    utils.find_xpath(browser, _locators.catalog).click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, _locators.book_locator))
    )

    utils.find(browser, _locators.book_locator).click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, _locators.button_add_to_cart))
    )
    button_to_add = browser.find_element_by_xpath(_locators.button_add_to_cart)
    assert button_to_add, "There is no button(("

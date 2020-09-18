from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as _locators


def search_item():
    # Data
    book_name = 'Google Hacking'
    book_locator = 'a[title="Google Hacking"]'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        # Steps
        browser.find_element_by_css_selector(_locators.input_search).send_keys(book_name)
        browser.find_element_by_css_selector(_locators.input_search_button).click()

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, book_locator))
        )

        # Assert
        book_name_text = browser.find_element_by_css_selector(book_locator).text
        assert book_name in book_name_text, \
            "Search item '%s' should contain text '%s'" % (book_name_text, book_name)

    finally:
        browser.quit()


search_item()

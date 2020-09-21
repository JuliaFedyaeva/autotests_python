from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as _locators
import test_data
import utils


def search_item():
    # Data
    book_locator = 'a[title="Google Hacking"]'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        # Steps
        utils.authorizaite(browser, test_data.book_name)

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, book_locator))
        )

        # Assert
        book_name_text = utils.find(browser, book_locator).text
        assert test_data.book_name in book_name_text, \
            "Search item '%s' should contain text '%s'" % (book_name_text, test_data.book_name)

    finally:
        browser.quit()


search_item()

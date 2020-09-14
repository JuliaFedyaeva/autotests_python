from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # предусловие
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/ru')

    # ищем строку поиска и вводим название товара
    search = browser.find_element_by_id('id_q').send_keys('Google Hacking')
    searchButton = browser.find_element_by_css_selector('input[value = "Найти"]').click()

    # проверяем, что на странице появился искомый товар
    waitLoading = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[title="Google Hacking"]'))
    )

    bookName = browser.find_element_by_css_selector('a[title="Google Hacking"]').text
    assert 'Google Hacking' in bookName

finally:
    time.sleep(5)
    browser.quit()

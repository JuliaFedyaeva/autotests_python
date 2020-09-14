from selenium import webdriver
import time

try:
    #### предусловия
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/ru')

    email = 'julia.fedyaeva@mail.ru'

    # открываем страницу с авторизацией
    registrationButton = browser.find_element_by_id('login_link').click()

    # проверяем, что открылась нужная страница
    pageAuthDetector = browser.find_element_by_css_selector('form#login_form h2').text
    assert 'Войти' in pageAuthDetector

    #### шаги
    # находим ссылку восстановления пароля и кликаем на неё
    remindPassword = browser.find_element_by_css_selector('a[href="/ru/password-reset/"]').click()

    # проверяем, что открылась нужная страница
    passwordPageDetector = browser.find_element_by_css_selector('div.page-header.action h1').text
    assert 'Восстановление пароля' in passwordPageDetector

    # заполняем форму
    emailInput = browser.find_element_by_id('id_email').send_keys(email)

    buttonAuthorisation = browser.find_element_by_xpath('//button[contains(text(), "Отправить письмо для смены пароля")]').click()

    #### проверка финального ОР
    successMessage = browser.find_element_by_css_selector('div.page-header.action h1').text

    assert 'Письмо отправлено' in successMessage

finally:
    time.sleep(5)
    browser.quit()

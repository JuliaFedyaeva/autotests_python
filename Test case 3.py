from selenium import webdriver
import time

try:
    # предусловия
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/ru')

    #  тут должны быть данные, которые есть в системе
    email = 'me@mail.ru'
    password = 'nekakuvseh123'

    # шаги
    # открываем страницу с авторизацией
    registrationButton = browser.find_element_by_id('login_link').click()

    # проверяем, что открылась нужная страница
    pageDetector = browser.find_element_by_css_selector('form#login_form h2').text
    assert 'Войти' in pageDetector

    # заполняем форму
    emailInput = browser.find_element_by_id('id_login-username').send_keys(email)

    passwordInput = browser.find_element_by_id('id_login-password').send_keys(password)

    buttonAuthorisation = browser.find_element_by_css_selector('button[value="Log In"]').click()

    # проверка финального ОР
    sucsessMessage = browser.find_element_by_css_selector('div.alertinner.wicon').text

    assert 'Рады видеть вас снова' in sucsessMessage


finally:
    time.sleep(5)
    browser.quit()



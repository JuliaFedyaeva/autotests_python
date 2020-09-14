from selenium import webdriver
import time

try:
    # предусловия
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/ru')

    #  тут по идее должен быть рандомайзер какой-то с тестовыми данными из списка
    email = 'its_me@mail.ru'
    password = 'nekakuvseh123'

    # шаги
    # открываем страницу с регистрацией
    registrationButton = browser.find_element_by_id('login_link').click()

    # проверяем, что открылась нужная страница
    pageDetector = browser.find_element_by_css_selector('form#register_form h2').text
    assert "Зарегистрироваться" in pageDetector

    # заполняем форму
    emailInput = browser.find_element_by_id('id_registration-email').send_keys(email)

    passwordInput = browser.find_element_by_id('id_registration-password1').send_keys(password)

    repeatPasswordInput = browser.find_element_by_id('id_registration-password2').send_keys(password)

    buttonRegistration = browser.find_element_by_css_selector('button[value="Register"]').click()

    # проверка финального ОР
    sucsessMessage = browser.find_element_by_css_selector('div.alertinner.wicon').text

    assert "Спасибо за регистрацию!" in sucsessMessage


finally:
    time.sleep(5)
    browser.quit()



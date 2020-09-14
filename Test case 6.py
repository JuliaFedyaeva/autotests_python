from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    #### предусловия
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/ru')

    name = "Max"
    lastname = "Payne"
    email = 'me@mail.ru'
    password = 'nekakuvseh123'
    address = 'PlayStation'
    city = 'Nowhere'
    postcode = '652877'

    # авторизуемся
    registrationButton = browser.find_element_by_id('login_link').click()

    # проверяем, что открылась нужная страница
    pageAuthDetector = browser.find_element_by_css_selector('form#login_form h2').text
    assert 'Войти' in pageAuthDetector

    # заполняем форму авторизации
    emailInput = browser.find_element_by_id('id_login-username').send_keys(email)
    passwordInput = browser.find_element_by_id('id_login-password').send_keys(password)
    buttonAuthorisation = browser.find_element_by_css_selector('button[value="Log In"]').click()

    # проверка аторизации
    successMessage = browser.find_element_by_css_selector('div.alertinner.wicon').text

    assert 'Рады видеть вас снова' in successMessage

    # открываем страницу с каталогом товаров
    catalogPage = browser.find_element_by_xpath('//a[contains(text(), "Все товары")]').click()

    # проверяем, что открылась страница каталога
    pageCatalogDetector = browser.find_element_by_css_selector('div.page-header.action h1').text
    assert 'Все товары' in pageCatalogDetector

    # находим ссылку добавления товара в корзину и кликаем на неё
    addToCart = browser.find_element_by_xpath('//button[contains(text(), "Добавить в корзину")]').click()

    # проверяем сообщение об отправке
    addToCartMessage = browser.find_element_by_css_selector('div.alertinner').text
    assert 'был добавлен в вашу корзину' in addToCartMessage

    whatIsInCart = browser.find_element_by_css_selector('div.alertinner strong').text

    # посмотрим, что в корзине
    cartLink = browser.find_element_by_css_selector('a[href="/ru/basket/"]').click()

    cart = browser.find_element_by_css_selector('h3 a').text

    # проверка корзины
    assert whatIsInCart == cart

    #### шаги
    # переходим к оформлению заказа
    checkout = browser.find_element_by_xpath('//a[contains(text(), "Перейти к оформлению")]').click()

    # чекаем, где мы находимся
    pageShippingAddressDetected = browser.find_element_by_css_selector('div.sub-header h1').text
    assert "Адрес доставки" in pageShippingAddressDetected

    # заполняем поля доставки
    inputName = browser.find_element_by_id('id_first_name').send_keys(name)
    inputLastname = browser.find_element_by_id('id_last_name').send_keys(lastname)
    inputAddress = browser.find_element_by_id('id_line1').send_keys(address)
    inputCity = browser.find_element_by_id('id_line4').send_keys(city)
    inputPostcode = browser.find_element_by_id('id_postcode').send_keys(postcode)

    select = Select(browser.find_element_by_id('id_country'))
    select.select_by_value('RU')

    buttonToContinue = browser.find_element_by_xpath('//button[contains(text(), "Продолжить")]').click()

    # тут по идее должна быть проверка способа доставки, но нет такого раздела почему-то,
    # сразу перекидывает на шаг оплаты

    # проверка невозможности продолжить оформление покупки без оплаты
    pagePaymentDetector = browser.find_element_by_css_selector('div.sub-header h1').text
    assert "Введите параметры платежа" in pagePaymentDetector

    #здесь поля оплаты остаются пустыми

    #### проверяем ОР
    # проверяем, что кнопка не активна
    buttonDisabled = buttonToContinue.getAttribute('disabled')
    assert buttonDisabled == "true"

    # пытаемся продолжить оформление заказа, надеюсь, безуспешно)
    buttonToContinue.click()

finally:
    time.sleep(5)
    browser.quit()

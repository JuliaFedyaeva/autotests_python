from selenium import webdriver


def add_product_to_cart():
    try:
        #### предусловия
        browser = webdriver.Chrome()
        browser.get('http://selenium1py.pythonanywhere.com/ru')

        # открываем страницу с каталогом товаров
        catalogPage = browser.find_element_by_xpath('//a[contains(text(), "Все товары")]').click()

        # проверяем, что открылась страница каталога
        pageCatalogDetector = browser.find_element_by_css_selector('div.page-header.action h1').text
        assert 'Все товары' in pageCatalogDetector

        #### шаги
        # находим ссылку добавления товара в корзину и кликаем на неё
        addToCart = browser.find_element_by_xpath('//button[contains(text(), "Добавить в корзину")]').click()

        # проверяем сообщение об отправке
        addToCartMessage = browser.find_element_by_css_selector('div.alertinner').text
        assert 'был добавлен в вашу корзину' in addToCartMessage

        whatIsInCart = browser.find_element_by_css_selector('div.alertinner strong').text

        # посмотрим, что в корзине
        cartLink = browser.find_element_by_css_selector('a[href="/ru/basket/"]').click()

        cart = browser.find_element_by_css_selector('h3 a').text

        #### проверка финального ОР
        assert whatIsInCart == cart

    finally:
        browser.quit()




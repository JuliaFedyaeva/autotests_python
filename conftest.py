import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose your language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if browser_language == "ru":
        print("\nstart chrome browser for test..")
        browser.get('http://selenium1py.pythonanywhere.com/ru/')
    elif browser_language == "fr":
        print("\nstart firefox browser for test..")
        browser.get('http://selenium1py.pythonanywhere.com/fr/')
    elif browser_language == "es":
        print("\nstart firefox browser for test..")
        browser.get('http://selenium1py.pythonanywhere.com/es/')
    else:
        raise pytest.UsageError("--browser_language should be selected")
    yield browser
    print("\nquit browser..")
    browser.quit()

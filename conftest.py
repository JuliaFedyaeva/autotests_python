import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose your language")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    if browser_language is None: raise pytest.UsageError('test run should contain language fo test')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})

    print("\nstart chrome document for test..")
    document = webdriver.Chrome(options=options)
    document.implicitly_wait(5)

    yield document
    print("\nquit document..")
    document.quit()

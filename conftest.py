import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--enable-javascript')
    _driver = webdriver.Chrome(options=options)
    _driver.get('https://practice-automation.com/form-fields/')
    yield _driver
    _driver.quit()

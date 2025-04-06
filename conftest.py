import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver

    driver.quit()

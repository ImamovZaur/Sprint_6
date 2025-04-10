import pytest
from selenium import webdriver
from data import Urls
from pages.logo_page import LogoPage
from pages.order_page import OrderPage
from pages.question_page import QuestionPage

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver

    driver.quit()

@pytest.fixture()
def page_logo(driver):
    page_logo = LogoPage(driver)
    return page_logo

@pytest.fixture()
def order_page(driver):
    page = OrderPage(driver)
    return page

@pytest.fixture()
def question_page(driver):
    page = QuestionPage(driver)
    return page
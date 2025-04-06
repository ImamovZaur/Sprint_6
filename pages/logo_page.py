import allure
from data import Urls
from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as eс

class LogoPage:

    @allure.step('клик по кнопке Заказать в шапке')
    def click_order_button(self, driver):
        driver.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()

    @allure.step('Клик по лого самокат')
    def click_scooter_logo(self, driver):
        driver.find_element(*LogoLocator.SCOOTER_LOGO).click()

    @allure.step('Клик по лого Яндекс')
    def click_yandex_logo(self, driver):
        driver.find_element(*LogoLocator.YANDEX_LOGO).click()

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self, browser):
        browser.switch_to.window(browser.window_handles[1])

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self, browser):
        WebDriverWait(browser, 10).until(eс.url_to_be(Urls.DZEN_PAGE))

    @allure.step('Проверка URL Дзена')
    def check_dzen_url(self, driver):
        assert driver.current_url == Urls.DZEN_PAGE

    @allure.step('Проверка URL главной страницы Самоката')
    def check_main_page_url(self, driver):
        assert driver.current_url == Urls.MAIN_PAGE
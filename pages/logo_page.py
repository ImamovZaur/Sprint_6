import allure
from pages.base_page import BasePage
from data import Urls
from locators.order_locators import OrderLocators
from locators.logo_locators import LogoLocator
from selenium.webdriver.support import expected_conditions as EC


class LogoPage(BasePage):

    @allure.step('клик по кнопке Заказать в шапке')
    def click_order_button(self):
       self.click_element(OrderLocators.ORDER_BUTTON_HEADER)

    @allure.step('Клик по лого самокат')
    def click_scooter_logo(self):
        self.click_element(LogoLocator.SCOOTER_LOGO)

    @allure.step('Клик по лого Яндекс')
    def click_yandex_logo(self):
        self.click_element(LogoLocator.YANDEX_LOGO)

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self):
        self.switch_window()

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self):
        self.wait_load(locator=Urls.DZEN_PAGE, time=10, condition=EC.url_to_be)

    @allure.step('Проверка URL Дзена')
    def check_dzen_url(self):
        assert self.get_current_url() == Urls.DZEN_PAGE

    @allure.step('Проверка URL главной страницы Самоката')
    def check_main_page_url(self):
        assert self.get_current_url() == Urls.MAIN_PAGE
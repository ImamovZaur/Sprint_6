import allure
from pages.logo_page import LogoPage

class TestLogo:
    page_logo = LogoPage()

    @allure.title('Проверка URL логотипа Самокат')
    def test_scooter_logo_url(self, driver):
        self.page_logo.click_order_button(driver)
        self.page_logo.click_scooter_logo(driver)
        self.page_logo.check_main_page_url(driver)

    @allure.title('Проверка URL логотипа Яндекс')
    def test_yandex_logo_url(self, driver):
        self.page_logo.click_order_button(driver)
        self.page_logo.click_yandex_logo(driver)
        self.page_logo.switching_to_the_tab(driver)
        self.page_logo.wait_for_page_load(driver)
        self.page_logo.check_dzen_url(driver)
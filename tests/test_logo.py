import allure

class TestLogo:

    @allure.title('Проверка URL логотипа Самокат')
    def test_scooter_logo_url(self, page_logo):
        page_logo.click_order_button()
        page_logo.click_scooter_logo()
        page_logo.check_main_page_url()

    @allure.title('Проверка URL логотипа Яндекс')
    def test_yandex_logo_url(self, page_logo):
        page_logo.click_order_button()
        page_logo.click_yandex_logo()
        page_logo.switching_to_the_tab()
        page_logo.wait_for_page_load()
        page_logo.check_dzen_url()
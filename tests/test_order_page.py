import allure
import pytest
from data import OrderData
from pages.order_page import OrderPage


class TestOrderPage:
    page = OrderPage()

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_top_button', OrderData.FIRST_ORDER), ('click_centre_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, driver, data_order, button_method):
        getattr(self.page, button_method)(driver)
        self.page.user_rent_order(driver, **data_order)
        self.page.confirmation_window(driver)
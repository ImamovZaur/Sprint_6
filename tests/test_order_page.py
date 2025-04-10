import allure
import pytest
from data import OrderData


class TestOrderPage:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_top_button', OrderData.FIRST_ORDER), ('click_centre_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, order_page, data_order, button_method):
        getattr(order_page, button_method)()
        order_page.user_rent_order(**data_order)
        order_page.confirmation_window()
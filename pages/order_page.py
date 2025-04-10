import allure
from pages.base_page import BasePage
from locators.order_locators import OrderLocators


class OrderPage(BasePage):
    @allure.step('Принятие куки')
    def click_cookie_accept(self):
        self.click_element(OrderLocators.COOKIE_ACCEPT)

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_top_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON_HEADER)

    @allure.step("Клик по кнопке Заказать в центре")
    def click_centre_button(self):
        self.scroll_element(OrderLocators.ORDER_CENTER_BUTTON)
        self.click_element(OrderLocators.ORDER_CENTER_BUTTON)

    @allure.step("Заполнение поля Имя")
    def user_name(self, name):
        self.send_text(OrderLocators.NAME, name)

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, last_name):
        self.send_text(OrderLocators.LAST_NAME, last_name)

    @allure.step("Заполнение поля Адрес")
    def user_address(self, address):
        self.send_text(OrderLocators.ADDRESS, address)

    @allure.step("Заполнение поля Метро")
    def metro(self, metro):
        self.send_text(OrderLocators.METRO, metro)
        self.click_element(OrderLocators.LIST_STATION)

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, phone):
        self.send_text(OrderLocators.NUMBER, phone)

    @allure.step('Клик по кнопке "Далее" в форме информации о пользователе')
    def click_next_button(self):
        self.click_element(OrderLocators.NEXT_BUTTON)

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, data):
        self.send_date(OrderLocators.DATE_DELIVERY, data)

    @allure.step("Заполнение поля Время аренды")
    def rental_time(self, day):
        self.click_element(OrderLocators.RENT_TIME)
        select_rent_time_locator = (OrderLocators.SELECT_RENT_TIME[0], OrderLocators.SELECT_RENT_TIME[1].format(day))
        self.click_element(select_rent_time_locator)

    @allure.step("Выбор цвета")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            self.click_element(OrderLocators.BLACK_COLOR_CHECKBOX)
        elif color == 'серая безысходность':
            self.click_element(OrderLocators.GREY_COLOR_CHECKBOX)

    @allure.step("Заполнение поля Комментарии к заказу")
    def enter_comment(self, comment):
        self.send_text(OrderLocators.COMMENT, comment)

    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self):
        self.click_element(OrderLocators.ORDER_BUTTON)

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_confirmation_button(self):
        self.click_element(OrderLocators.YES_BUTTON)

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        text = self.get_text(OrderLocators.ORDER_COMPLETED)
        assert 'Заказ оформлен' in text

    @allure.step("Полный позитивный сценарий")
    def user_rent_order(self, name, last_name, address, metro, number, delivery_date, rent_days, colour, comment):
        self.click_cookie_accept()
        self.user_name(name)
        self.user_last_name(last_name)
        self.user_address(address)
        self.metro(metro)
        self.user_phone(number)
        self.click_next_button()
        self.date_of_delivery(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.enter_comment(comment)
        self.click_order_button()
        self.click_confirmation_button()
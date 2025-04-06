import allure
from locators.order_locators import OrderLocators
from selenium.webdriver.common.keys import Keys


class OrderPage:
    @allure.step('Принятие куки')
    def click_cookie_accept(self, driver):
        driver.find_element(*OrderLocators.COOKIE_ACCEPT).click()

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_top_button(self, driver):
        driver.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()

    @allure.step("Клик по кнопке Заказать в центре")
    def click_centre_button(self, driver):
        element = driver.find_element(*OrderLocators.ORDER_CENTER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    @allure.step("Заполнение поля Имя")
    def user_name(self, driver, name):
        driver.find_element(*OrderLocators.NAME).send_keys(name)

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, driver, last_name):
        driver.find_element(*OrderLocators.LAST_NAME).send_keys(last_name)

    @allure.step("Заполнение поля Адрес")
    def user_address(self, driver, address):
        driver.find_element(*OrderLocators.ADDRESS).send_keys(address)

    @allure.step("Заполнение поля Метро")
    def metro(self, driver, metro):
        driver.find_element(*OrderLocators.METRO).send_keys(metro)
        driver.find_element(*OrderLocators.LIST_STATION).click()

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, driver, phone):
        driver.find_element(*OrderLocators.NUMBER).send_keys(phone)

    @allure.step('Клик по кнопке "Далее" в форме информации о пользователе')
    def click_next_button(self, driver):
        driver.find_element(*OrderLocators.NEXT_BUTTON).click()

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, driver, data):
        driver.find_element(*OrderLocators.DATE_DELIVERY).send_keys(data, Keys.ENTER)

    @allure.step("Заполнение поля Время аренды")
    def rental_time(self, driver, day):
        driver.find_element(*OrderLocators.RENT_TIME).click()
        select_rent_time_locator = (OrderLocators.SELECT_RENT_TIME[0], OrderLocators.SELECT_RENT_TIME[1].format(day))
        driver.find_element(*select_rent_time_locator).click()

    @allure.step("Выбор цвета")
    def checkbox_color(self, driver, color):
        if color == 'чёрный жемчуг':
            driver.find_element(*OrderLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            driver.find_element(*OrderLocators.GREY_COLOR_CHECKBOX).click()

    @allure.step("Заполнение поля Комментарии к заказу")
    def enter_comment(self, driver, comment):
        driver.find_element(*OrderLocators.COMMENT).send_keys(comment)

    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self, driver):
        driver.find_element(*OrderLocators.ORDER_BUTTON).click()

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_confirmation_button(self, driver):
        driver.find_element(*OrderLocators.YES_BUTTON).click()

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self, driver):
        text = driver.find_element(*OrderLocators.ORDER_COMPLETED).text
        assert 'Заказ оформлен' in text

    @allure.step("Полный позитивный сценарий")
    def user_rent_order(self, driver, name, last_name, address, metro, number, delivery_date, rent_days, colour, comment):
        self.click_cookie_accept(driver)
        self.user_name(driver, name)
        self.user_last_name(driver, last_name)
        self.user_address(driver, address)
        self.metro(driver, metro)
        self.user_phone(driver, number)
        self.click_next_button(driver)
        self.date_of_delivery(driver, delivery_date)
        self.rental_time(driver, rent_days)
        self.checkbox_color(driver, colour)
        self.enter_comment(driver, comment)
        self.click_order_button(driver)
        self.click_confirmation_button(driver)
from selenium.webdriver.common.by import By

class LogoLocator:
    YANDEX_LOGO = [By.XPATH, './/a[@href = "//yandex.ru"]']
    SCOOTER_LOGO = [By.XPATH, './/a[@href = "/"]']
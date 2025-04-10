from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_load(self, locator, time, condition):
        WebDriverWait(self.driver, time).until(condition(locator))

    def send_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_element(self, locator):
        element = self.find_elements(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_current_url(self):
        return self.driver.current_url

    def send_date(self, locator, date):
        self.driver.find_element(*locator).send_keys(date, Keys.ENTER)
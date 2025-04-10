from selenium.webdriver.common.by import By

class QuestionLocator:
    QUESTION =[By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]
    QUESTION_LIST = [By.CLASS_NAME, "accordion"]
    COOKIE_ACCEPT = (By.XPATH, ".//button[text()='да все привыкли']")
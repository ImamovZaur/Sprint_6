import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.question_locators import QuestionLocator

class QuestionPage:
    @allure.step('Принятие куки')
    def click_cookie_accept(self, driver):
        driver.find_element(*QuestionLocator.COOKIE_ACCEPT).click()

    @allure.step('Скролл до списка вопросов')
    def scroll_question_list(self, driver):
        element = driver.find_element(*QuestionLocator.QUESTION_LIST)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Текст вопроса')
    def get_question(self, driver, index):
        question_locator = (QuestionLocator.QUESTION[0], QuestionLocator.QUESTION[1].format(index))
        question = WebDriverWait(driver, 3).until(ec.element_to_be_clickable(question_locator))
        question.click()
        return question.text
    
    @allure.step('Текст ответа')
    def get_answer(self, driver, index):
        answers_locator = (QuestionLocator.ANSWER[0], QuestionLocator.ANSWER[1].format(index))
        answers = driver.find_element(*answers_locator)
        return answers.text
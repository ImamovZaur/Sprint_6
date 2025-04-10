import allure
from pages.base_page import BasePage
from locators.question_locators import QuestionLocator
from selenium.webdriver.support import expected_conditions as EC

class QuestionPage(BasePage):
    @allure.step('Принятие куки')
    def click_cookie_accept(self):
        self.click_element(QuestionLocator.COOKIE_ACCEPT)

    @allure.step('Скролл до списка вопросов')
    def scroll_question_list(self):
        self.scroll_element(QuestionLocator.QUESTION_LIST)

    @allure.step('Текст вопроса')
    def get_question(self, index):
        question_locator = (QuestionLocator.QUESTION[0], QuestionLocator.QUESTION[1].format(index))
        self.wait_load(locator=question_locator, time=10, condition=EC.element_to_be_clickable)
        self.click_element(question_locator)
        return self.get_text(question_locator)
    
    @allure.step('Текст ответа')
    def get_answer(self, index):
        answers_locator = (QuestionLocator.ANSWER[0], QuestionLocator.ANSWER[1].format(index))
        return self.get_text(answers_locator)
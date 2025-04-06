import allure
import pytest
from pages.question_page import QuestionPage
from data import QuestionsAndAnswers

class TestQuestionPage:
    page = QuestionPage()

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTION_AND_ANSWER)
    def test_check_question_and_answer(self, driver, index, question, answer):
        self.page.click_cookie_accept(driver)
        self.page.scroll_question_list(driver)
        question_text = self.page.get_question(driver, index)
        answer_text = self.page.get_answer(driver, index)
        assert question_text == question
        assert answer_text == answer
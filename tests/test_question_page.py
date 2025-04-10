import allure
import pytest
from data import QuestionsAndAnswers


class TestQuestionPage:

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTION_AND_ANSWER)
    def test_check_question_and_answer(self, question_page, index, question, answer):
        question_page.click_cookie_accept()
        question_page.scroll_question_list()
        question_text = question_page.get_question(index)
        answer_text = question_page.get_answer(index)
        assert question_text == question
        assert answer_text == answer
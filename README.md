# Sprint_6
## Тестовые сценарии

1. Выпадающий список в разделе «Вопросы о важном». 

Тебе нужно проверить: когда нажимаешь на стрелочку, открывается соответствующий текст. Важно написать отдельный тест на каждый вопрос.
2. Заказ самоката.

Нужно проверить весь флоу позитивного сценария с двумя наборами данных. Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу.
### Из чего состоит позитивный сценарий:
1. Нажать кнопку «Заказать». На странице две кнопки заказа.
2. Заполнить форму заказа.
3. Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
4. Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
5. Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.

Нужно написать тесты с разными данными: минимум два набора. Какие именно данные использовать — на твоё усмотрение. Сценарий общий, несмотря на разные точки входа: не нужно дважды тестировать каждую из них.


# Содержание проекта

1. allure_results - папка с отчетами Allure
2. locators - содержит локаторы для тестируемых страниц
- logo_locators.py - локаторы для логотипа Яндекс Самокат
- order_locators.py - локаторы для страницы оформления заказа
- question_locators.py - локаторы для раздела "Вопросы о важном"
3. pages - содержит Page Object для тестируемых страниц
- logo_page.py - page object для страницы логотипов
- order_page.py - page object для страницы заказа самоката
- question_page.py - page object для раздела "Вопросы о важном"
4. tests - содержит файлы с тестами
- test_logo - тесты для логотипа Яндекс Самокат
- test_order_page - тесты для страницы оформления закза
- test_question_page - тесты для раздела "Вопросы о важном"
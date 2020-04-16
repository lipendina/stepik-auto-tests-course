# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
# Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
# Ваша задача - реализовать автотест со следующим сценарием действий:
# 1) открыть страницу
# 2) ввести правильный ответ
# 3) нажать кнопку "Отправить"
# 4) дождаться фидбека о том, что ответ правильный
# 5) проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

from selenium import webdriver
import pytest
import time
import math

result = ''


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print(result)


@pytest.mark.parametrize('num', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_links(num, browser):
    global result
    link = f"https://stepik.org/lesson/{num}/step/1"
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    browser.get(link)
    area = browser.find_element_by_tag_name("textarea")
    area.send_keys(str(answer))
    btn = browser.find_element_by_tag_name("button")
    btn.click()
    text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == text
    except AssertionError:
        result += text

# У нас уже есть простой тест из предыдущего шага, который проверяет возможность зарегистрироваться на сайте.
# Однако разработчики решили немного поменять верстку страницы, чтобы она выглядела более современной.
# Обновленная страница доступна по другой ссылке. К сожалению, в процессе изменений они случайно внесли баг
# в форму регистрации.
# Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку.
# Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы
# и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо.

from selenium import webdriver

link = [
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html"
]

for i in link:
    browser = webdriver.Chrome()
    browser.get(i)

    input1 = browser.find_element_by_css_selector("div.first_block div.first_class input")
    input1.send_keys("Татьяна")
    input2 = browser.find_element_by_css_selector("div.first_block div.second_class input")
    input2.send_keys("Ковалева")
    input3 = browser.find_element_by_css_selector("div.first_block div.third_class input")
    input3.send_keys("t@yandex.ru")
    # input4 = browser.find_element_by_class_name("")
    input4 = browser.find_element_by_css_selector("div.second_block div.first_class input")
    input4.send_keys("+7(909)999-99-99")
    input5 = browser.find_element_by_css_selector("div.second_block div.second_class input")
    input5.send_keys("ул. Мира, 10")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

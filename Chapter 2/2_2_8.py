# В этом задании в форме регистрации требуется загрузить текстовый файл.
#
# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

import time
import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Tatiana")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Kovaleva")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("t.kovaleva@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

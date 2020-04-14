# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
# который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:
#
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return math.log(abs(12*math.sin(int(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(str(y))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    robot_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot_checkbox.click()
    robots_rule = browser.find_element_by_css_selector("[for='robotsRule']")
    robots_rule.click()
    button.click()

finally:
    time.sleep(30)
    browser.quit()

# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
# Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки
# с изображением сундука.
#
# Ваша программа должна:
#
# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

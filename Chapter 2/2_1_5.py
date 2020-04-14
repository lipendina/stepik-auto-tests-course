#Открыть страницу http://suninjuly.github.io/math.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "I'm the robot".
#Выбрать radiobutton "Robots rule!".
#Нажать на кнопку Submit.

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    robot_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot_checkbox.click()

    robots_rule = browser.find_element_by_css_selector("[for='robotsRule']")
    robots_rule.click()

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

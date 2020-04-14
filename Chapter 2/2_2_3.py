# Для этой задачи мы придумали еще один вариант капчи для роботов.
# Придется немного переобучить нашего робота, чтобы он справился с новым заданием.
#
# Напишите код, который реализует следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element_by_id("num1")
    a = a_element.text
    b_element = browser.find_element_by_id("num2")
    b = b_element.text
    s = int(a) + int(b)

    answer_list = Select(browser.find_element_by_id("dropdown"))
    answer_list.select_by_value(str(s))

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

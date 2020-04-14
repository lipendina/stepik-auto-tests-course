# На этот раз воспользуемся возможностью искать элементы по XPath.
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации,
# как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки.
# Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё.

import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Tatiana")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Kovaleva")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

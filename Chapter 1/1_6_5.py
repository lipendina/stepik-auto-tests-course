# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

# Добавьте в самый верх своего кода import math
# Добавьте команду в код, которая откроет страницу: http://suninjuly.github.io/find_link_text
# Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
# str(math.ceil(math.pow(math.pi, math.e)*10000))
# Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
# Заполните скриптом форму так же как вы делали в предыдущем шаге урока
# После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание

import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    by_text_link = browser.find_element_by_link_text(text)
    by_text_link.click()

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Tatiana")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Kovaleva")
    input3 = browser.find_element_by_name("firstname")
    input3.send_keys("Moscow")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

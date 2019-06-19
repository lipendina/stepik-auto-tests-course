#Возьмите тесты из шага 10 - https://stepik.org/lesson/138920/step/10?unit=196194
#Создайте новый файл
#Создайте в нем класс тестов unittest
#Добавьте тест для страницы http://suninjuly.github.io/registration1.html﻿
#Добавьте второй тест для страницы http://suninjuly.github.io/registration2.html
#Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
#Запустите получившиеся тесты из файла
#Второй тест должен так же падать, как и в оригинальном задании 1_5_10

import unittest
import time
from selenium import webdriver

class TestAbs(unittest.TestCase):
    browser = webdriver.Chrome()
    def checkingPage(self, link):

        self.browser.get(link)

        input1 = self.browser.find_element_by_css_selector("div.first_block div.first_class input")
        input1.send_keys("Татьяна")
        input2 = self.browser.find_element_by_css_selector("div.first_block div.second_class input")
        input2.send_keys("Ковалева")
        input3 = self.browser.find_element_by_css_selector("div.first_block div.third_class input")
        input3.send_keys("t@yandex.ru")
        input4 = self.browser.find_element_by_css_selector("div.second_block div.first_class input")
        input4.send_keys("+7(909)999-99-99")
        input5 = self.browser.find_element_by_css_selector("div.second_block div.second_class input")
        input5.send_keys("ул. Мира, 10")
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        successful_registration = self.browser.find_element_by_tag_name("h1")
        success = successful_registration.text
        return success

    def testOfLink1(self):
        link = "http://suninjuly.github.io/registration1.html"
        success = self.checkingPage(link)
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", success)

    def testOfLink2(self):
        link = "http://suninjuly.github.io/registration2.html"
        success = self.checkingPage(link)
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", success)

if __name__ == "__main__":
    unittest.main()

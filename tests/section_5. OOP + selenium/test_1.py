import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_1:
    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

test = Test_1()
test.test_select_product()
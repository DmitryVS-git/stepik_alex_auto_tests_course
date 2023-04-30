from test_3_login_page import Login_page

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_1:
    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        login_standard_user = 'standard_user'
        password_all = 'secret_sauce'

        driver.get(base_url)
        driver.maximize_window()

        print('Start test')

        login = Login_page(driver)
        login.authorization(login_standard_user, password_all)

        button_select_product = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack')))
        button_select_product.click()
        print('Click Select Product')

        enter_shopping_cart = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'shopping_cart_container')))
        enter_shopping_cart.click()
        print('Go to shopping cart')

        success_test = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.title')))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart', 'Texts are different!'

        time.sleep(2)

        print('Test Success!')



test = Test_1()
test.test_select_product()
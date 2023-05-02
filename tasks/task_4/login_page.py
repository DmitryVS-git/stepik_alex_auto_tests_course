import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_page:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'user-name')))
        password = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'password')))
        login_btn = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, 'login-button')))

        print('============== Login ==============')
        # Fill LogIn inputs
        user_name.send_keys(login_name)
        print('Input login')
        password.send_keys(login_password)
        print('Input password')
        # click login button
        login_btn.click()
        print('Click Login Button')
        print('=========== FINISH Login ==========\n')


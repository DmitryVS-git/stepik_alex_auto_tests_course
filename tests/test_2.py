import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
login_standard_user = 'standard_use'
password_all = 'secret_sauce'


try:
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    user_name = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    login_btn = driver.find_element(By.ID, 'login-button')

    user_name.send_keys(login_standard_user)
    print('Input login')

    password.send_keys(password_all)
    print('Input password')

    login_btn.click()
    print('Click Login Button')
    time.sleep(2)

    warning_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    warning_msg_text = warning_msg.text

    assert warning_msg_text == 'Epic sadface: Username and password do not match any user in this service'

    driver.refresh()

finally:
    driver.quit()
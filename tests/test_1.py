import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
login_standard_user = 'standard_user'
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

    # text_products = driver.find_element(By.XPATH, "//span[@class='title']")
    #
    # value_text_products = text_products.text
    #
    # assert value_text_products == 'Products', 'Element not found'

    url = 'https://www.saucedemo.com/inventory.html'
    get_url = driver.current_url
    print(get_url)
finally:
    driver.quit()
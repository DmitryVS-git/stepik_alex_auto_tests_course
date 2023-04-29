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

    menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    menu.click()
    time.sleep(2)

    link_about = driver.find_element(By.ID, 'about_sidebar_link')
    link_about.click()
    time.sleep(2)

    current_title = driver.title

    assert current_title == 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing', 'Title is different'

    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)


finally:
    driver.quit()
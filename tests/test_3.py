import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import Select

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
    password.send_keys(Keys.RETURN)
    time.sleep(2)

    filter = driver.find_element(By.XPATH, "//select")
    filter.click()
    time.sleep(2)
    filter.send_keys(Keys.DOWN)
    time.sleep(2)
    filter.send_keys(Keys.RETURN)
    time.sleep(2)
    filter = Select(driver.find_element(By.XPATH, "//select"))
    filter.select_by_index(1)

    date_now = datetime.datetime.now().strftime("%Y.%m.%d %H.%M.%S")
    name_screenshot = f'screenshot_{date_now}'
    driver.save_screenshot(f".\\..\\screenshots\\{name_screenshot}.png")


finally:
    driver.quit()
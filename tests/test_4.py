import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

    # driver.execute_script('window.scrollTo(0, 200)')
    action = ActionChains(driver)
    link_linkedin = driver.find_element(By.CSS_SELECTOR, '.social_linkedin a')
    action.move_to_element(link_linkedin).perform()
    time.sleep(2)

    date_now = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = f'screenshot{date_now}'
    driver.save_screenshot(f".\\screenshots\\{name_screenshot}.png")

finally:
    driver.quit()
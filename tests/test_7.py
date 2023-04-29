import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/checkbox'
login_standard_user = 'standard_user'
password_all = 'secret_sauce'


try:
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    checkbox = driver.find_element(By.CSS_SELECTOR, '.rct-checkbox')
    checkbox.click()
    time.sleep(2)
    expand_toggle = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
    expand_toggle.click()
    time.sleep(2)


finally:
    driver.quit()
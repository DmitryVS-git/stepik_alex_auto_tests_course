import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/radio-button'

try:
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    # action = ActionChains(driver)

    checkbox_yes = driver.find_element(By.ID, 'yesRadio')
    checkbox_yes.click()
    time.sleep(2)
except ElementClickInterceptedException as exception:
    checkbox_yes = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    checkbox_yes.click()
    time.sleep(2)









finally:
    driver.quit()
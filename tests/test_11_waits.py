import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/dynamic-properties'

try:
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # btn_vivible = driver.find_element(By.ID, 'visibleAfter')
    # btn_vivible.click()

    btn_visible = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'visibleAfter')))
    btn_visible.click()











finally:
    driver.quit()
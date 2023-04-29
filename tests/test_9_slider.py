import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
base_url = 'https://the-internet.herokuapp.com/horizontal_slider'

try:
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    actions = ActionChains(driver)

    slider_image = driver.find_element(By.CSS_SELECTOR, 'input')
    actions.click_and_hold(slider_image).move_by_offset(100, 0).release().perform()
    actions.click_and_hold(slider_image).move_by_offset(-100, 0).release().perform()
    time.sleep(2)

finally:
    driver.quit()
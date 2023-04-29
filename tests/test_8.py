import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/buttons'


try:
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    action = ActionChains(driver)

    double_click_btn = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    right_click_btn = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
    click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")

    action.double_click(double_click_btn).perform() # Выполняем двойной клик
    action.context_click(right_click_btn).perform() # Выполняем правый клик
    click_btn.click()
    time.sleep(2)



finally:
    driver.quit()
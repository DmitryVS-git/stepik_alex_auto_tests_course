import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'


try:
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    input_select_date = driver.find_element(By.ID, 'datePickerMonthYearInput')
    input_select_date.click()
    time.sleep(2)
    now_date = datetime.datetime.now().strftime('%d')
    print(now_date)
    date = str(int(now_date) + 1)
    locator = f"//div[@aria-label='Choose Saturday, April {date}th, 2023']"
    date_29 = driver.find_element(By.XPATH, locator)
    date_29.click()
    time.sleep(2)
    # input_select_date.click()
    # date_today = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    # date_today.click()
    # time.sleep(2)

    # input_select_date_text = input_select_date.get_attribute('value')
    # print(input_select_date_text)
    # input_select_date.send_keys(Keys.BACKSPACE*len(input_select_date_text))
    # input_select_date.send_keys('12/12/1993')
    # time.sleep(2)
    # input_select_date.send_keys(Keys.RETURN)
    # time.sleep(2)



finally:
    driver.quit()
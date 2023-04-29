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
    print("Go to website\n")

    # Get input_select_date
    input_select_date = driver.find_element(By.ID, 'datePickerMonthYearInput')

    # Get today date and the day after 10 days
    date_today = datetime.datetime.today()
    date_10_days_from_today = (date_today + datetime.timedelta(days=10)).strftime('%m/%d/%Y')
    print(f"Current date: {date_today.strftime('%m/%d/%Y')}\n"
          f"Date after 10 days: {date_10_days_from_today}\n")

    # Clear the input date
    input_select_date.send_keys(Keys.CONTROL + "A")
    input_select_date.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    print("Clear the input date\n")

    # Enter new date
    input_select_date.send_keys(date_10_days_from_today)
    input_select_date.send_keys(Keys.RETURN)

    # Assert final date
    value_input_select_date = input_select_date.get_attribute('value')
    assert value_input_select_date == date_10_days_from_today, "Dates are different!"
    time.sleep(2)

    print("SUCCESS!")
finally:
    driver.quit()
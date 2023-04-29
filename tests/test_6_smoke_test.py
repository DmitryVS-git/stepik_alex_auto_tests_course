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

    '''Info Product №1'''
    product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    value_product_1 = product_1.text
    print(value_product_1)

    price_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']/preceding-sibling::div")
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)

    select_product_1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    select_product_1.click()
    print('Select product_1')

    shopping_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    value_shopping_cart = shopping_cart.text

    assert int(value_shopping_cart) == 1, 'Shopping badge value is different'

    shopping_cart.click()
    time.sleep(2)

    '''Info cart Product 1'''
    cart_product_1 = driver.find_element(By.ID, "item_4_title_link")
    value_cart_product_1 = cart_product_1.text
    print(value_cart_product_1)

    assert value_cart_product_1 == value_product_1, "Product's names are different!"

    cart_price_product_1 = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']/preceding-sibling::div")
    value_cart_price_product_1 = cart_price_product_1.text
    print(value_cart_price_product_1)

    assert value_price_product_1 == value_cart_price_product_1, "Pdoduct's prices are different!"

    time.sleep(2)

    button_checkout = driver.find_element(By.ID, 'checkout')
    button_checkout.click()
    print('Click checkout button')
    time.sleep(2)

    '''Select User Info'''
    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")

    first_name.send_keys('Dmitry')
    last_name.send_keys('Smirnov')
    zip_code.send_keys('4154109')

    button_continue = driver.find_element(By.ID, 'continue')
    button_continue.click()

#     Checkout overview
    finish_cart_product_1 = driver.find_element(By.ID, "item_4_title_link")
    value_finish_cart_product_1 = finish_cart_product_1.text
    print(value_finish_cart_product_1)

    finish_price_product_1 = driver.find_element(By.CSS_SELECTOR, ".item_pricebar")
    value_finish_price_product_1 = finish_price_product_1.text
    print(value_finish_price_product_1)

    price_total = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
    value_price_total = price_total.text
    print(value_price_total)


    item_total = f"Item total: {value_finish_price_product_1}"
    print(item_total)

    assert value_product_1 == value_finish_cart_product_1, 'Different product names!'
    assert value_price_total == item_total, 'Different prices!'


finally:
    driver.quit()
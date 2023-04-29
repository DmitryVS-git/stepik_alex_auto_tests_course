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

    print('################### Log In #####################')
    user_name.send_keys(login_standard_user)
    print('Input login')
    password.send_keys(password_all)
    print('Input password')
    login_btn.click()
    print('Click Login Button')
    time.sleep(2)
    print('################################################\n')

#   Info Product_1
    print('################### Info product 1 #####################')
    product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
    value_product_1 = product_1.text
    print(value_product_1)

    price_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']/preceding-sibling::div")
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)

    select_product_1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    select_product_1.click()
    print('Select product_1')
    print('########################################################\n')

#   Info Product_2
    print('################### Info product 2 #####################')
    product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
    value_product_2 = product_2.text
    print(value_product_2)

    price_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']/preceding-sibling::div")
    value_price_product_2 = price_product_2.text
    print(value_price_product_2)

    select_product_2 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    select_product_2.click()
    print('Select product_2')
    print('########################################################\n')
    time.sleep(2)

#   Shopping Cart badge assert
    print('################### Check Shopping Cart values #####################')
    shopping_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    value_shopping_cart = shopping_cart.text

    assert int(value_shopping_cart) == 2, 'Shopping badge value is different'
    print('SUCCESS')
    print('###################################################################\n')

    shopping_cart.click()
    time.sleep(2)

#   Info cart Product 1
    print('################### CHECK Products in Shopping cart inside #####################')
    print('################### Product_1 #####################')
    cart_product_1 = driver.find_element(By.ID, "item_4_title_link")
    value_cart_product_1 = cart_product_1.text
    print(value_cart_product_1)

    assert value_cart_product_1 == value_product_1, "Product_1 name != Cart product_1 name"

    cart_price_product_1 = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-backpack']/preceding-sibling::div")
    value_cart_price_product_1 = cart_price_product_1.text
    print(value_cart_price_product_1)

    assert value_price_product_1 == value_cart_price_product_1, "Product_1 price != Cart product_1 price"
    print('###################################################\n')

#   Info cart Product 2
    print('################### Product_2 #####################')
    cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
    value_cart_product_2 = cart_product_2.text
    print(value_cart_product_2)

    assert value_cart_product_2 == value_product_2, "Product_2 name != Cart product_2 name"

    cart_price_product_2 = driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bolt-t-shirt']/preceding-sibling::div")
    value_cart_price_product_2 = cart_price_product_2.text
    print(value_cart_price_product_2)
    assert value_price_product_2 == value_cart_price_product_2, "Product_2 price != Cart product_2 price"
    print('###################################################\n')

    print('SUCCESS')
    print('################################################################################\n')


    button_checkout = driver.find_element(By.ID, 'checkout')
    button_checkout.click()
    print('Click checkout button\n')

#   Page "Checkout: Your Information"
    print('################### Fill the form #####################')

    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")

    first_name.send_keys('Dmitry')
    last_name.send_keys('Smirnov')
    zip_code.send_keys('4154109')

    button_continue = driver.find_element(By.ID, 'continue')
    button_continue.click()
    print('SUCCESS')
    print('######################################################\n')


#   Checkout overview
    print('################### Checkout overview #####################')

    print('################### Product_1 #####################')
    finish_cart_product_1 = driver.find_element(By.ID, "item_4_title_link")
    value_finish_cart_product_1 = finish_cart_product_1.text
    print(value_finish_cart_product_1)

    finish_price_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/following-sibling::div[@class='item_pricebar']")
    value_finish_price_product_1 = finish_price_product_1.text
    print(value_finish_price_product_1)
    print('###################################################\n')

    print('################### Product_2 #####################')
    finish_cart_product_2 = driver.find_element(By.ID, "item_1_title_link")
    value_finish_cart_product_2 = finish_cart_product_2.text
    print(value_finish_cart_product_2)

    finish_price_product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']/following-sibling::div[@class='item_pricebar']")
    value_finish_price_product_2 = finish_price_product_2.text
    print(value_finish_price_product_2)
    print('###################################################\n')

#   Assert names
    print('################### Check names of products #####################')
    assert value_finish_cart_product_1 == value_finish_cart_product_1, "Product_1 name != Cart_product_1 name"
    assert value_finish_cart_product_2 == value_finish_cart_product_2, "Product_2 name != Cart_product_2 name"

    print('SUCCESS')
    print('#################################################################\n')


#   Price total
    print('################### Check total price of products #####################')
    price_total = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
    value_price_total = price_total.text
    print(value_price_total)
    print('#######################################################################\n')

#   Assert prices
    print('################### Final Assert Prices #####################')
    prices = [value_finish_price_product_1, value_finish_price_product_2]

    value_finish_price_products = sum(map(float, [price.lstrip('$') for price in prices]))
    items_total = f"Item total: ${value_finish_price_products}"

    assert items_total == value_price_total, 'Finish price products != total price'
    print('Total summary price is good')
    print('#############################################################')


#
#
#     item_total = f"Item total: {value_finish_price_product_1}"
#     print(item_total)
#
#     assert value_product_1 == value_finish_cart_product_1, 'Different product names!'
#     assert value_price_total == item_total, 'Different prices!'


finally:
    driver.quit()
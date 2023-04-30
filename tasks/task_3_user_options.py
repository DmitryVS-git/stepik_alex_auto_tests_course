from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
login_standard_user = 'standard_user'
password_all = 'secret_sauce'


try:
    driver.get(base_url)
    driver.maximize_window()

    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'login-button')))

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
    print('################################################\n')

    #   User chooses a product
    print('################### User choice #####################')
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title')))

    list_products = driver.find_elements(By.CSS_SELECTOR, '.inventory_item')
    list_products_names = [(i.find_element(By.CSS_SELECTOR, '.inventory_item_name')).text for i in list_products]
    list_products_prices = [(i.find_element(By.CSS_SELECTOR, '.inventory_item_price')).text for i in list_products]

    print('Приветствуем Вас в нашем интернет-магазине!\n')
    while True:
        print('=============== Список товаров ===============')
        for index, name in enumerate(list_products_names):
            print(f'{index + 1}) {name}: {list_products_prices[index]}')
        print()
        user_choice = int(input('Пожалуйста, выберите из списка выше один товар, указав его номер: '))

        if user_choice in range(1, len(list_products)+1):
            product_name = list_products_names[user_choice-1]
            product_price = list_products_prices[user_choice-1]
            print(f'Ваш выбор: {product_name}: {product_price}')
            break
        print(f'Вы ввели неверное значение. пожалуйста, введите цифру от 1 до {len(list_products)}\n')

    print('#####################################################\n')

    print('################### Add the chosen item to cart #####################')
    buttons_add_to_cart = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
    button_select_user_product = buttons_add_to_cart[user_choice-1]

    button_select_user_product.click()
    print('Select product')

    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.shopping_cart_badge')))

    shopping_cart = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge')
    value_shopping_cart = shopping_cart.text

    assert int(value_shopping_cart) == 1, 'Shopping badge value is different'

    shopping_cart.click()
    print('#####################################################################\n')

#   Info cart product
    print('################### Assert cart product and user chosen product #####################')
    cart_product = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name")
    value_cart_product = cart_product.text
    print(value_cart_product)

    assert value_cart_product == product_name, "Product's names are different!"

    cart_price_product = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
    value_cart_price_product = cart_price_product.text
    print(value_cart_price_product)

    assert value_cart_price_product == product_price, "Pdoduct's prices are different!"

    button_checkout = driver.find_element(By.ID, 'checkout')
    button_checkout.click()
    print('Click checkout button')
    print('#####################################################################################\n')

#   Select user info
    print('################### Enter user info #####################')
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.checkout_info')))

    first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    zip_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")

    first_name.send_keys('Dmitry')
    print('Enter first name')
    last_name.send_keys('Smirnov')
    print('Enter last name')
    zip_code.send_keys('4154109')
    print('Enter zip code')

    button_continue = driver.find_element(By.ID, 'continue')
    button_continue.click()
    print('Click btn to continue')
    print('#########################################################\n')

#   Checkout overview
    print('################### Checkout overview #####################')
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, 'checkout_summary_container')))

    finish_cart_product_name = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name")
    value_finish_cart_product_name = finish_cart_product_name.text
    print(f'Cart product name: {value_finish_cart_product_name}')

    finish_cart_product_price = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price")
    value_finish_cart_product_price = finish_cart_product_price.text
    print(f'Cart product price: {value_finish_cart_product_price}')

    price_total = driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
    value_price_total = price_total.text
    print(f'Cart price item total — {value_price_total}')

    item_total = f"Item total: {value_finish_cart_product_price}"
    print(item_total, end='\n')

    print('Checking finally product name and product price')

    assert product_name == value_finish_cart_product_name, 'Different product names!'
    assert value_price_total == item_total, 'Different prices!'
    print('###########################################################\n')

    print('SUCCESS!')

finally:
    driver.quit()
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

    #   User chooses a product
    list_products = driver.find_elements(By.CSS_SELECTOR, '.inventory_item')
    list_products_names = [(i.find_element(By.CSS_SELECTOR, '.inventory_item_name')).text for i in list_products]
    list_products_prices = [(i.find_element(By.CSS_SELECTOR, '.inventory_item_price')).text for i in list_products]
    # print(list_products_names)
    # print()
    # print(list_products_prices)
    print('Приветствуем Вас в нашем интернет-магазине!\n')
    print('=============== Список товаров ===============')
    # СДЕЛАТЬ ВСЁ ПРИ ПОМОЩИ БЕСКОНЕЧНОГО ЦИКЛА ПО СХЕМЕ DO WHILE!
    for index, name in enumerate(list_products_names):
        print(f'{index + 1}: {name}')
    user_choice = int(input('Пожалуйста, выберите из списка выше один товар, указав его номер: '))
    while user_choice not in range(1, len(list_products)):

        if user_choice in range(1, len(list_products)):
            print(f'Ваш выбор: {list_products_names[user_choice-1]}: {list_products_prices[user_choice-1]}')
            break







finally:
    driver.quit()
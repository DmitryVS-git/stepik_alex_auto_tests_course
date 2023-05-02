from login_page import LoginPage

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class Test1:
    def test_login(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        logins = ['standard_user', 'problem_user', 'locked_out_user', 'performance_glitch_user']
        password_all = 'secret_sauce'

        driver.get(base_url)
        driver.maximize_window()

        print('++++++++++++++++ Start Test_1 ++++++++++++++++\n')

        login_page = LoginPage(driver)

        for login in logins:
            # Authorization
            login_page.authorization(login, password_all)

            print(f'****************Test login "{login}" - STARTED!****************')

            # Checking different logins from [logins]
            match login:
                case 'standard_user' | 'problem_user' | 'performance_glitch_user':
                    # Check title 'Products'
                    products_title = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
                    products_title_text = products_title.text
                    # Assert title's text
                    assert products_title_text == 'Products', 'Different titles!'
                    print('Login SUCCESS!')
                    print('Headings match!')
                    # LogOut
                    button_burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
                    button_burger_menu.click()

                    logout_burger_menu = WebDriverWait(driver, 2).until(
                        EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
                    logout_burger_menu.click()

                case 'locked_out_user':
                    # Get error msg and close it
                    error_msg = WebDriverWait(driver, 2).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
                    print('Error message appeared')

                    button_close_error = driver.find_element(By.CSS_SELECTOR, '.error-button')
                    button_close_error.click()
                    # Assert error_msg is disappeared
                    assert WebDriverWait(driver, 2).until(EC.invisibility_of_element(error_msg)) is True
                    print('Error message disappeared')
                    # Clear LogIn inputs
                    username = driver.find_element(By.ID, 'user-name')
                    username.send_keys(Keys.CONTROL + "A")
                    username.send_keys(Keys.BACKSPACE)

                    password = driver.find_element(By.ID, 'password')
                    password.send_keys(Keys.CONTROL + "A")
                    password.send_keys(Keys.BACKSPACE)
                    # Assert inputs is cleared
                    assert len(username.get_attribute('value')) == 0 and len(username.get_attribute('value')) == 0
                    print('Inputs cleared!')

            print(f'****************Test login "{login}" - FINISHED!****************\n')

        print('Test_1 Success!')
        print('++++++++++++++++ FINISH Test_1 ++++++++++++++++\n')


test = Test1()
test.test_login()

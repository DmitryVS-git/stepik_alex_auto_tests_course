from login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test1:
    driver = webdriver.Chrome()
    problem_users = []

    # Check title 'Products'
    def check_title(self):
        products_title = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        products_title_text = products_title.text
        # Assert title's text
        assert products_title_text == 'Products', 'Different titles!'
        print('Login SUCCESS!')
        print('Headings match!')

    # LogOut
    def logOut(self):
        button_burger_menu = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        button_burger_menu.click()
        logout_burger_menu = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_burger_menu.click()

    def test_login(self):
        base_url = 'https://www.saucedemo.com/'
        logins = ['standard_user', 'problem_user', 'locked_out_user', 'performance_glitch_user']
        password_all = 'secret_sauce'

        self.driver.get(base_url)
        self.driver.maximize_window()

        print('++++++++++++++++ Start Test_1 ++++++++++++++++\n')

        login_page = LoginPage(self.driver)

        for login in logins:
            # Authorization
            print(f'****************Test login "{login}" - STARTED!****************')
            login_page.authorization(login, password_all)

            try:
                self.check_title()
                self.logOut()
            except:
                print(f'!!!!!!!!- User with login "{login}" isn\'t authorized -!!!!!!!!')
                self.problem_users.append(login)
                self.driver.refresh()

            print(f'****************Test login "{login}" - FINISHED!****************\n')

        if self.problem_users:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Test_1 partially successful !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print(f'There are problems with user/users: {self.problem_users}')
        else:
            print('Test_1 Success!')
        print('++++++++++++++++ FINISH Test_1 ++++++++++++++++\n')


test = Test1()
test.test_login()

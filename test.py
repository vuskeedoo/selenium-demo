import unittest
from selenium import webdriver
import page

class SeleniumAutomation(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome('C:/webdriver/chromedriver')
        self.driver.get('http://automationpractice.com/index.php')

    def test_login_with_valid_email(self):
        """Login with valid email and password"""
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches('My Store'), 'Website title does not match'
        main_page.go_to_login_page()
        main_page.enter_account_info('vuskeedoo@email.com', '12345')
        assert main_page.is_title_matches('My account - My Store'), 'Login failed'
        main_page.logout_account()

    def test_login_with_invalid_email(self):
        """Login with invalid email and invalid password"""
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches('My Store'), 'Website title does not match'
        main_page.go_to_login_page()
        main_page.enter_account_info('vuskeedoo', '1234')
        assert main_page.is_title_matches('Login - My Store'), 'Website title does not match'
        assert main_page.check_login_error() == 'Invalid email address.'

    def test_login_with_invalid_password(self):
        """Login with valid email and invalid password"""
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches('My Store'), 'Website title does not match'
        main_page.go_to_login_page()
        main_page.enter_account_info('vuskeedoo@asd.com', '1234')
        assert main_page.is_title_matches('Login - My Store'), 'Website title does not match'
        assert main_page.check_login_error() == 'Invalid password.'

    def xtest_add_item_to_cart(self):
        """Adding first item on home page to cart"""
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches('My Store'), 'Website title does not match'
        main_page.add_item_to_cart()
        main_page.proceed_to_checkout()
        assert main_page.verify_cart_page('Shopping-cart Summary'), 'Shopping cart error'

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, AccountProfileLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Testing login and shopping cart functionality"""
    def is_title_matches(self, title):
        return title in self.driver.title

    def go_to_login_page(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((MainPageLocators.LOGIN_BUTTON)))
        element.click()

    def enter_account_info(self, email, password):
        wait = WebDriverWait(self.driver, 10)
        email_input = wait.until(EC.element_to_be_clickable((LoginPageLocators.EMAIL_ADDRESS)))
        email_input.send_keys(email)
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)
        submit_input = self.driver.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        submit_input.click()

    def logout_account(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((AccountProfileLocators.LOGOUT_BUTTON)))
        element.click()

    def check_login_error(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_ERROR)
        #print("Login Error Message: %s" % (element.text))
        return(element.text)

    def add_item_to_cart(self):
        element = self.driver.find_element(*MainPageLocators.ADD_ITEM)
        element.click()

    def proceed_to_checkout(self):
        element = self.driver.find_element(*MainPageLocators.PROCEED_BUTTON)
        element.click()

    def verify_cart_page(self, title):
        element = self.driver.find_element(*MainPageLocators.CART_TITLE)
        return title in element

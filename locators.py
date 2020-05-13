from selenium.webdriver.common.by import By

"""CLASS_NAME, CSS_SELECTOR, ID,LINK_TEXT, NAME, PARTIAL_LINK_TEXT, TAG_NAME, XPATH"""

class MainPageLocators(object):
    """Home page locators"""
    LOGIN_BUTTON = (By.CLASS_NAME, 'login')
    ADD_ITEM = (By.CSS_SELECTOR, 'a[data-id-product="1"]')
    PROCEED_BUTTON = (By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')

class LoginPageLocators(object):
    """Login page locators"""
    EMAIL_ADDRESS = (By.ID, 'email')
    PASSWORD = (By.ID, 'passwd')
    LOGIN_SUBMIT = (By.ID, 'SubmitLogin')
    LOGIN_ERROR = (By.CSS_SELECTOR, 'div[class="alert alert-danger"] li')

class AccountProfileLocators(object):
    """After login (profile page) locators"""
    LOGOUT_BUTTON = (By.CLASS_NAME, 'logout')

class CartLocators(object):
    """Shopping cart locators"""
    CART_TITLE = (By.CSS_SELECTOR, 'h1[id="cart_title"]')

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import LOGIN_PAGE_URL

class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators() 


    def open(self):
        self.open_url(LOGIN_PAGE_URL)
 
        self.wait_until_clickable(self.locators.EMAIL_INPUT)




    def enter_email(self, email):
        email_field = self.find_element(self.locators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.find_element(self.locators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        
        btn = self.wait_until_clickable(self.locators.LOGIN_WITH_CRED_BUTTON)
        btn.click()

    def click_recovery_password_link(self):

        link = self.wait_until_clickable(self.locators.RECOVERY_PASSWORD_LINK)
        link.click()
        self.wait_url_contains("forgot-password", timeout=15)
  

    def get_error_message(self, timeout=10):
        element = self.find_element(self.locators.ERROR_MESSAGE, timeout=timeout)
        return element.text
    
    def is_user_logged_in(self, timeout=15):
        locator = self.locators.ORDER_BUTTON
        
        self.wait_until_visible(locator, timeout=timeout)
        return self.is_element_present_now(locator)
    
    def go_to_order_history(self):
        link = self.wait_until_clickable(self.locators.ORDER_HISTORY_LINK)
        link.click()

    
   
    def logout(self):
        self.wait_for_logout_button_clickable()
        btn = self.wait_until_clickable(self.locators.LOGOUT_BUTTON)
        btn.click()




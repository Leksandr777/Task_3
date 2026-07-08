from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators() 


    def open(self):
        login_url = f"{self.base_url}login"
        self.driver.get(login_url)
 
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

        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.RECOVERY_PASSWORD_LINK)
        )
        link.click()

        WebDriverWait(self.driver, 15).until(
            lambda d: "forgot-password" in d.current_url
        )

        return self

    def get_error_message(self):
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).text
    
    def is_user_logged_in(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.ORDER_BUTTON)) is not None
    
    def go_to_order_history(self):
        link = self.wait_until_clickable(self.locators.ORDER_HISTORY_LINK)
        link.click()
        return self
    
    def logout(self):
        self.wait_for_logout_button_clickable()
        btn = self.wait_until_clickable(self.locators.LOGOUT_BUTTON)
        btn.click()
        return self
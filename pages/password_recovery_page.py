from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constant import RESET_PASSWORD_URL

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryLocators()  

    def click_recovery_password_link(self):
        link = self.wait_until_clickable(self.locators.RECOVERY_PASSWORD_LINK, timeout=10)
        link.click()
        return self

    def enter_email(self, email):
        self.wait_until_visible(self.locators.PAGE_TITLE, timeout=10)

        email_field = self.wait_until_visible(self.locators.EMAIL_INPUT, timeout=10)
        
        email_field.click()
        
        email_field.clear()
        email_field.send_keys(email)
        return self

    def click_recovery_button(self):
        button = self.wait_until_clickable(self.locators.RECOVERY_BUTTON, timeout=10)
        button.click()
        self.wait_url_contains(RESET_PASSWORD_URL, timeout=20)
        return self

    def get_email_input_value(self):
        field = self.find_element(self.locators.EMAIL_INPUT, timeout=5)
        return field.get_attribute("value")
    
    def wait_for_page_load(self):
        self.wait_until_visible(self.locators.PAGE_TITLE, timeout=10)
        return self
    
    def click_show_password(self):

        button = self.wait_until_clickable(self.locators.SHOW_PASSWORD_BUTTON, timeout=10)
        button.click()
        return self
from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryLocators()  

    def click_recovery_password_link(self):
        link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.RECOVERY_PASSWORD_LINK)
        )
        link.click()
        return self

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.PAGE_TITLE)
        )

        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.EMAIL_INPUT)
        )
        
        email_field.click()
        
        email_field.clear()
        email_field.send_keys(email)
        return self

    def click_recovery_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.RECOVERY_BUTTON)
        )
        button.click()
        WebDriverWait(self.driver, 20).until(
            lambda d: "/reset-password" in d.current_url
    )
        return self

    def get_email_input_value(self):
        field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.locators.EMAIL_INPUT)
        )
        return field.get_attribute("value")
    
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.PAGE_TITLE)
        )
        return self
    
    def click_show_password(self):

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.SHOW_PASSWORD_BUTTON)
        )
        button.click()

        return self
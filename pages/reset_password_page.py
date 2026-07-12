from locators.reset_password_locators import ResetPasswordLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResetPasswordLocators()

    def wait_for_page_load(self):
        self.find_element(self.locators.PASSWORD_INPUT, timeout=20)
        self.find_element(self.locators.SHOW_PASSWORD_BUTTON, timeout=20)
        return self

    def enter_password(self, password):
        password_field = self.find_element(self.locators.PASSWORD_INPUT, timeout=10)
        password_field.send_keys(password)
        return password_field

    def click_show_password(self):
        show_button = self.wait_until_clickable(self.locators.SHOW_PASSWORD_BUTTON, timeout=10)
        show_button.click()
        return self
    
    def get_password_input_element(self):
        return self.find_element(self.locators.PASSWORD_INPUT) 
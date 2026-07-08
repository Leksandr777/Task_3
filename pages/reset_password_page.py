from locators.reset_password_locators import ResetPasswordLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ResetPasswordLocators()

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.locators.PASSWORD_INPUT)
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.locators.SHOW_PASSWORD_BUTTON)
        )

    def enter_password(self, password):
        password_field = self.driver.find_element(*self.locators.PASSWORD_INPUT)
        password_field.send_keys(password)
        return password_field

    def click_show_password(self):
        show_button = self.driver.find_element(*self.locators.SHOW_PASSWORD_BUTTON)
        show_button.click()
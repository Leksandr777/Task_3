
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = "https://qa-stellarburgers.education-services.ru/"

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_until_clickable(self, locator, timeout=15):  
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_url_to_be(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )

    def wait_until_visible(self, locator, timeout=15):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
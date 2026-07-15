
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import BASE_URL


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = BASE_URL

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
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

    def open_url(self, url: str):
        self.driver.get(url)

    def wait_relative_url_to_be(self, path: str, timeout=10):
        expected_url = f"{self.base_url}{path}"
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def wait_url_contains(self, substring: str, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: substring in d.current_url
        )

    def wait_until_not(self, condition, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(condition)

    def execute_script(self, script: str, *args):
        return self.driver.execute_script(script, *args)
    
    def wait_until_backdrop_disappears(self, locator, timeout=10):
        self.wait_until_not(
            EC.invisibility_of_element_located(locator),
            timeout=timeout
        )


    def wait_text_to_be_present_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )
    
    def wait_until_text_not_equal(self, locator, text, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: self.wait_until_visible(locator, timeout=1).text.strip() != text
        )


    def get_current_url(self) -> str:
        return self.driver.current_url
    

    def wait_until_element_disappears(self, locator, timeout=15):
 
        self.wait_until_not(
            EC.presence_of_element_located(locator),
            timeout=timeout
        )


    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    

    def wait_until_at_least_one_element(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(self.find_elements(locator, timeout=1)) > 0
        )


    def is_url_contains(self, substring):
        return substring in self.driver.current_url
    
    def is_element_present_now(self, locator):
        by, value = locator
        elements = self.driver.find_elements(by, value)
        return len(elements) > 0

    def get_password_input_value(self):
        field = self.find_element(self.locators.PASSWORD_INPUT, timeout=5)
        return field.get_attribute("value")
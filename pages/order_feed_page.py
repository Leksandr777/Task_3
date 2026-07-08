from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    def wait_for_orders_list(self):

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.ORDERS_LIST)
        )
        return self

    def open_first_order_details(self):

        self.wait_for_orders_list()
        
        first_order = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.FIRST_ORDER)
        )
        first_order.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.ORDER_DETAILS_MODAL)
        )

        order_number_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ORDER_NUMBER)
        )
        return order_number_elem.text
    
    def get_all_order_numbers_from_list(self) -> list[str]:

        WebDriverWait(self.driver, 30).until(
            lambda d: len(d.find_elements(*self.locators.ORDER_NUMBER_IN_LIST)) > 0
        )

        numbers_elements = self.driver.find_elements(*self.locators.ORDER_NUMBER_IN_LIST)
        return [el.text.strip() for el in numbers_elements]

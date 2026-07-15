from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    def wait_for_orders_list(self):

        self.find_element(self.locators.ORDERS_LIST, timeout=10)


    def open_first_order_details(self):

        self.wait_for_orders_list()
        
        first_order = self.wait_until_clickable(self.locators.FIRST_ORDER, timeout=10)
        first_order.click()

        self.find_element(self.locators.ORDER_DETAILS_MODAL, timeout=10)

        order_number_elem = self.wait_until_visible(self.locators.ORDER_NUMBER, timeout=10)
        return order_number_elem.text
    
    def get_all_order_numbers_from_list(self) -> list[str]:

        self.wait_until_at_least_one_element(self.locators.ORDER_NUMBER_IN_LIST, timeout=30 )

        numbers_elements = self.find_elements(self.locators.ORDER_NUMBER_IN_LIST, timeout=10)
        return [el.text.strip() for el in numbers_elements]

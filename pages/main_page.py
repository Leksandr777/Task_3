from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.Ingredient_modal_locators import IngredientModalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from selenium.webdriver.common.action_chains import ActionChains
from constant import FEED_URL,FULL_FEED_URL

class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.modal_locators = IngredientModalLocators()

    def open(self):
        self.open_url(self.base_url)
        self.find_element(self.locators.CONSTRUCTOR_BUTTON, timeout=10)

    def go_to_personal_cabinet(self):
        btn = self.wait_until_clickable(self.locators.PERSONAL_CABINET_LINK)
        btn.click()


    def go_to_order_history(self):
    
        link = self.wait_until_clickable(self.locators.ORDER_HISTORY_LINK)
        link.click()


    def logout(self):

        logout_btn = self.wait_until_clickable(self.locators.LOGOUT_BUTTON)
        logout_btn.click()

    
    def waiting_for_user_logged_in(self):
        self.find_element(self.locators.ORDER_BUTTON, timeout=10) is not None

    
    def wait_for_logout_button_clickable(self):

        self.wait_until_clickable(self.locators.LOGOUT_BUTTON)

    
    def go_to_feed(self):

        btn = self.wait_until_clickable(self.locators.FEED_BUTTON)
        btn.click()

        self.wait_url_contains(FEED_URL, timeout=15)

    def go_to_constructor(self):
        btn = self.wait_until_clickable(self.locators.CONSTRUCTOR_BUTTON)
        btn.click()

        self.wait_until_visible(self.locators.CONSTRUCTOR_HEADER)

    
    def open_ingredient_modal(self, ingredient_locator):


        ingredient_btn = self.wait_until_clickable(ingredient_locator, timeout=20)
        ingredient_btn.click()
  
        self.wait_until_visible(self.modal_locators.MODAL_TITLE, timeout=20)
        self.wait_url_contains("/ingredient/", timeout=20)

    
    def close_ingredient_modal(self):

        close_btn = self.wait_until_clickable(self.modal_locators.CLOSE_BUTTON, timeout=20)
        close_btn.click()

        self.wait_until_backdrop_disappears(self.modal_locators.MODAL_BACKDROP, timeout=20)

        self.wait_until_visible(self.locators.CONSTRUCTOR_HEADER, timeout=20)
    

    def get_ingredient_counter_value(self):

        counter_el = self.wait_until_visible(self.locators.INGREDIENT_COUNTER, timeout=10)
        return int(counter_el.text)
    

    def drag_and_drop_ingredient(self, ingredient_locator, drop_area_locator):
        self.find_element(self.locators.INGREDIENTS_LIST, timeout=10)

        ingredient_el = self.wait_until_clickable(ingredient_locator, timeout=15)
        drop_area_el = self.wait_until_visible(drop_area_locator, timeout=15)
        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            ingredient_el
        )
        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            drop_area_el
        )
        initial_counter = self.wait_until_visible(self.locators.INGREDIENT_COUNTER, timeout=10)
        initial_value = int(initial_counter.text)
        expected_value = str(initial_value + 1)

        # Это обходит сломанную реализацию ActionChains в Firefox
        js_drag_script = """
            var src = arguments[0];
            var tgt = arguments[1];
            
            // 1. Начало перетаскивания
            src.dispatchEvent(new DragEvent('dragstart', {bubbles: true, cancelable: true}));
            
            // 2. Вход в зону и сам DROP (самое важное для React)
            tgt.dispatchEvent(new DragEvent('dragenter', {bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('drop', {bubbles: true, cancelable: true}));
            
            // 3. Завершение
            src.dispatchEvent(new DragEvent('dragend', {bubbles: true, cancelable: true}));
        """
        
        self.execute_script(js_drag_script, ingredient_el, drop_area_el)

        self.wait_text_to_be_present_in_element(
            self.locators.INGREDIENT_COUNTER,
            expected_value,
            timeout=15
        )


    

    def click_order_button(self):
        order_button = self.wait_until_clickable(self.locators.ORDER_BUTTON, timeout=15)
        order_button.click()

    
    def wait_for_order_modal(self):
        self.wait_until_visible(self.locators.ORDER_ID, timeout=15)

    
    def get_order_id(self):

        el = self.wait_until_visible(self.locators.ORDER_ID, timeout=10)
        text = el.text.strip()
        return int(text)
    
    def get_modal_title(self):
        el = self.wait_until_visible(self.locators.MODAL_TITLE, timeout=10)
        return el.text.strip()

    def get_order_message(self):
        el = self.wait_until_visible(self.locators.ORDER_MESSAGE, timeout=10)
        return el.text.strip()
    

    def drag_first_bun_to_basket(self):

        bun = self.wait_until_clickable(self.locators.FIRST_BUN_INGREDIENT, timeout=10)
        drop_area = self.wait_until_visible(self.locators.DROP_AREA, timeout=10)

        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", bun)
        self.execute_script("arguments[0].scrollIntoView({block: 'center'});", drop_area)

        js_drag_script = """
            var src = arguments[0];
            var tgt = arguments[1];
            src.dispatchEvent(new DragEvent('dragstart', {bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('dragenter', {bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('drop', {bubbles: true, cancelable: true}));
            src.dispatchEvent(new DragEvent('dragend', {bubbles: true, cancelable: true}));
        """
        self.execute_script(js_drag_script, bun, drop_area)

        


    
    def place_order_and_close_modal(self) -> str:

        order_btn = self.wait_until_clickable(self.locators.ORDER_BUTTON, timeout=20)
        order_btn.click()

        order_id_elem = self.wait_until_visible(self.locators.ORDER_ID, timeout=20)

        self.wait_until_text_not_equal(
            self.locators.ORDER_ID,
            "9999",
            timeout=20
        )

        real_id = order_id_elem.text.strip()
        formatted_id = f"0{real_id}"

        close_btn = self.wait_until_clickable(self.locators.MODAL_CLOSE_BUTTON, timeout=20)
        self.execute_script("arguments[0].click();", close_btn)

        return formatted_id
    
    def go_to_profile_and_orders_history(self):


        cab_btn = self.wait_until_clickable(self.locators.PERSONAL_CABINET_LINK, timeout=10)
        cab_btn.click()

        history_btn = self.wait_until_clickable(self.locators.ORDER_HISTORY_LINK, timeout=10)
        history_btn.click()


    def get_feed_counters(self):

        current_url = self.get_current_url()
        if FEED_URL not in current_url:
            self.go_to_feed()


        total_el = self.wait_until_visible(OrderFeedLocators.TOTAL_ORDERS_COUNTER, timeout=15)
        today_el = self.wait_until_visible(OrderFeedLocators.TODAY_ORDERS_COUNTER, timeout=15)

        total = int(total_el.text.strip())
        today = int(today_el.text.strip())

        return total, today

    def go_to_main_and_wait_cabinet_link(self):

        self.open_url(self.base_url)
        self.find_element(self.locators.PERSONAL_CABINET_LINK, timeout=10)

    

    def wait_until_no_orders_message_disappears(self):
        self.wait_until_element_disappears(self.locators.NO_ORDERS_MESSAGE,timeout=15 )


    def get_orders_in_work(self):

        self.open_url(FULL_FEED_URL)


        self.find_element(OrderFeedLocators.ORDERS_LIST, timeout=20)

        self.wait_until_element_disappears(OrderFeedLocators.NO_ORDERS_MESSAGE,timeout=20)

        orders = self.find_elements(OrderFeedLocators.ORDERS_IN_WORK, timeout=20)
        return orders
    

    def is_constructor_loaded(self):

        return self.wait_until_visible(self.locators.CONSTRUCTOR_HEADER) is not None


    def open_first_sauce_modal(self):
        self.open_ingredient_modal(MainPageLocators.FIRST_SAUCE_INGREDIENT)


    def is_ingredient_modal_open(self):
        title = self.wait_until_visible(IngredientModalLocators.MODAL_TITLE)
        return title.text == "Детали ингредиента"

    def is_ingredient_modal_url_correct(self):

        return self.is_url_contains("/ingredient/")
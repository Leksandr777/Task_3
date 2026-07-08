from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.Ingredient_modal_locators import IngredientModalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
        self.modal_locators = IngredientModalLocators()

    def open(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.CONSTRUCTOR_BUTTON)
        )

    def go_to_personal_cabinet(self):
        btn = self.wait_until_clickable(self.locators.PERSONAL_CABINET_LINK)
        btn.click()
        return self

    def go_to_order_history(self):
    
        link = self.wait_until_clickable(self.locators.ORDER_HISTORY_LINK)
        link.click()
        return self

    def logout(self):

        logout_btn = self.wait_until_clickable(self.locators.LOGOUT_BUTTON)
        logout_btn.click()
        return self
    
    def waiting_for_user_logged_in(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.ORDER_BUTTON)) is not None
        return self
    
    def wait_for_logout_button_clickable(self):

        self.wait_until_clickable(self.locators.LOGOUT_BUTTON)
        return self
    
    def go_to_feed(self):

        btn = self.wait_until_clickable(self.locators.FEED_BUTTON)
        btn.click()


        WebDriverWait(self.driver, 15).until(
            EC.url_contains("/feed")
        )

    def go_to_constructor(self):
        btn = self.wait_until_clickable(self.locators.CONSTRUCTOR_BUTTON)
        btn.click()

        self.wait_until_visible(self.locators.CONSTRUCTOR_HEADER)
        return self
    
    def open_ingredient_modal(self, ingredient_locator):


        ingredient_btn = self.wait_until_clickable(ingredient_locator, timeout=20)
        ingredient_btn.click()
  
        self.wait_until_visible(self.modal_locators.MODAL_TITLE, timeout=20)

        WebDriverWait(self.driver, 20).until(EC.url_contains("/ingredient/"))
        return self
    
    def close_ingredient_modal(self):

        close_btn = self.wait_until_clickable(self.modal_locators.CLOSE_BUTTON, timeout=20)
        close_btn.click()

        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(self.modal_locators.MODAL_BACKDROP)
        )

        self.wait_until_visible(self.locators.CONSTRUCTOR_HEADER, timeout=20)
        return self

    def get_ingredient_counter_value(self):

        counter_el = self.wait_until_visible(self.locators.INGREDIENT_COUNTER, timeout=10)
        return int(counter_el.text)
    

    def drag_and_drop_ingredient(self, ingredient_locator, drop_area_locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators.INGREDIENTS_LIST)
        )

        ingredient_el = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(ingredient_locator)
        )
        drop_area_el = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(drop_area_locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", ingredient_el
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", drop_area_el
        )

        initial_counter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.INGREDIENT_COUNTER)
        )
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
        
        self.driver.execute_script(js_drag_script, ingredient_el, drop_area_el)

        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(
                self.locators.INGREDIENT_COUNTER,
                expected_value
            )
        )

        return self
    

    def click_order_button(self):
        order_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.locators.ORDER_BUTTON)
        )
        order_button.click()
        return self
    
    def wait_for_order_modal(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.locators.ORDER_ID)
        )
        return self
    
    def get_order_id(self):

        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ORDER_ID)
        )
        text = el.text.strip()
        return int(text)
    
    def get_modal_title(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.MODAL_TITLE)
        )
        return el.text.strip()

    def get_order_message(self):
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ORDER_MESSAGE)
        )
        return el.text.strip()
    

    def drag_first_bun_to_basket(self):
        # 1. Ждём элементы
        bun = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.FIRST_BUN_INGREDIENT)
        )
        drop_area = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.DROP_AREA)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", bun)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drop_area)

        js_drag_script = """
            var src = arguments[0];
            var tgt = arguments[1];
            src.dispatchEvent(new DragEvent('dragstart', {bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('dragenter', {bubbles: true, cancelable: true}));
            tgt.dispatchEvent(new DragEvent('drop', {bubbles: true, cancelable: true}));
            src.dispatchEvent(new DragEvent('dragend', {bubbles: true, cancelable: true}));
        """
        self.driver.execute_script(js_drag_script, bun, drop_area)

        
        return self

    
    def place_order_and_close_modal(self) -> str:
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 20)

        # Клик по кнопке заказа
        order_btn = wait.until(EC.element_to_be_clickable(self.locators.ORDER_BUTTON))
        order_btn.click()

        # Ждём появления элемента с номером заказа
        order_id_elem = wait.until(EC.visibility_of_element_located(self.locators.ORDER_ID))

        wait.until(lambda d: order_id_elem.text.strip() != "9999")

        # Берём уже реальный ID и добавляем ноль
        real_id = order_id_elem.text.strip()
        formatted_id = f"0{real_id}"

        # Закрываем модалку
        close_btn = wait.until(EC.element_to_be_clickable(self.locators.MODAL_CLOSE_BUTTON))
        self.driver.execute_script("arguments[0].click();", close_btn)

        return formatted_id
    
    def go_to_profile_and_orders_history(self):


        cab_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.PERSONAL_CABINET_LINK)
        )
        cab_btn.click()


        history_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.ORDER_HISTORY_LINK)
        )
        history_btn.click()
        return self

    def get_feed_counters(self):

        current_url = self.driver.current_url
        if "/feed" not in current_url:
            self.go_to_feed()

        from selenium.webdriver.support import expected_conditions as EC
        from locators.order_feed_locators import OrderFeedLocators

        wait = WebDriverWait(self.driver, 15)

        # Ждём видимости счётчиков (вместо голого find_element)
        total_el = wait.until(EC.visibility_of_element_located(OrderFeedLocators.TOTAL_ORDERS_COUNTER))
        today_el = wait.until(EC.visibility_of_element_located(OrderFeedLocators.TODAY_ORDERS_COUNTER))

        total = int(total_el.text.strip())
        today = int(today_el.text.strip())

        return total, today

    def go_to_main_and_wait_cabinet_link(self):

        self.driver.get(self.base_url)

        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.locators.PERSONAL_CABINET_LINK))
        return self
    

    def wait_until_no_orders_message_disappears(self):
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(self.driver, 15)
        wait.until_not(EC.presence_of_element_located(self.locators.NO_ORDERS_MESSAGE))
        return self

    def get_orders_in_work(self):
        from selenium.webdriver.support import expected_conditions as EC
        from locators.order_feed_locators import OrderFeedLocators

        wait = WebDriverWait(self.driver, 20)


        self.driver.get("https://qa-stellarburgers.education-services.ru/feed")


        wait.until(EC.presence_of_element_located(OrderFeedLocators.ORDERS_LIST))

        wait.until_not(EC.presence_of_element_located(OrderFeedLocators.NO_ORDERS_MESSAGE))

        # Получаем список заказов
        orders = self.driver.find_elements(*OrderFeedLocators.ORDERS_IN_WORK)
        return orders
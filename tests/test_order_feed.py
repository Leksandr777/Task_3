from pages.login_page import LoginPage
import pytest
import allure
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from helpers import create_user, delete_user
from selenium.webdriver.common.action_chains import ActionChains
from pages.order_feed_page import OrderFeedPage

@allure.feature("Лента заказов и синхронизация")
@pytest.mark.usefixtures("setup_pages_and_user")
class TestOrderFeed:


    @allure.story("Просмотр деталей первого заказа в ленте")
    def test_order_feed(self):

        self.main_page.open()
        self.main_page.go_to_feed()
        order_number = self.order_feed_page.open_first_order_details()

        assert order_number.startswith('#'), f"Номер заказа указан некорректно"
        
    @allure.story("Синхронизация заказов между историей и лентой")
    def test_orders_synchronization(self):
        # 1. Авторизация
        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()


        self.main_page.drag_first_bun_to_basket()

        created_order_id = self.main_page.place_order_and_close_modal()

        self.main_page.go_to_profile_and_orders_history()

        history_numbers = self.order_feed_page.get_all_order_numbers_from_list()

        self.main_page.go_to_feed()

        feed_numbers = self.order_feed_page.get_all_order_numbers_from_list()


        assert set(history_numbers).issubset(set(feed_numbers)), (
            f"Не все заказы из истории отображаются в ленте.\n"
            f"История: {history_numbers}\nЛента: {feed_numbers}"
        )
    
    @allure.story("Проверка увеличения счётчиков заказов после создания заказа")
    def test_counter_orders(self):

        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()


        initial_total, initial_today = self.main_page.get_feed_counters()

        self.main_page.go_to_main_and_wait_cabinet_link()


        self.main_page.go_to_constructor()

        self.main_page.drag_first_bun_to_basket()


        self.main_page.place_order_and_close_modal()

        final_total, final_today = self.main_page.get_feed_counters()

        assert final_total == initial_total + 1, (
            f"Счётчик всех заказов не увеличился: было {initial_total}, стало {final_total}"
        )
        assert final_today == initial_today + 1, (
            f"Счётчик заказов за сегодня не увеличился: было {initial_today}, стало {final_today}"
        )
        
    @allure.story("Заказ отображается в разделе «В работе»")        
    def test_order_in_work(self):
        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()


        self.main_page.drag_first_bun_to_basket()

        order_id = self.main_page.place_order_and_close_modal()


        self.main_page.go_to_feed()


        orders_texts = [o.text.strip() for o in self.main_page.get_orders_in_work()]

        assert str(order_id) in orders_texts, f"Заказ {order_id} не найден в ленте заказов"
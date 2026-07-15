import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.Ingredient_modal_locators import IngredientModalLocators

from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from helpers import create_user, delete_user
from constant import FEED_URL, INGREDIENT_URL

@allure.feature("Функционал главной страницы и конструктора")
@pytest.mark.usefixtures("setup_pages_and_user")
class TestMainFunc:


    @allure.story("Переход на ленту заказов (feed)")
    def test_step_to_feed(self):
        self.main_page.open()
        self.main_page.go_to_feed()

        assert self.main_page.is_url_contains(FEED_URL)

    @allure.story("Переход в конструктор бургеров")
    def test_step_to_constructor(self, browser):
        self.main_page.open()
        self.main_page.go_to_constructor()


        assert self.main_page.is_constructor_loaded(), "Конструктор не загрузился"

        assert self.main_page.is_url_contains(self.main_page.base_url)

    @allure.story("Открытие модального окна ингредиента")
    def test_ingredient_modal(self, browser):
        self.main_page.open()
        self.main_page.go_to_constructor()

        self.main_page.open_first_sauce_modal()


        answer =  self.main_page.is_ingredient_modal_open()
        assert answer is True, "Неверный заголовок модального окна"

        assert self.main_page.is_ingredient_modal_url_correct()


    @allure.story("Увеличение счётчика ингредиентов при драге")
    def test_ingredient_counter_increase(self, browser):
        self.main_page.open()
        self.main_page.go_to_constructor()

        initial_value = self.main_page.get_ingredient_counter_value()

        self.main_page.drag_and_drop_ingredient(
            self.main_page.locators.FIRST_SAUCE_INGREDIENT,
            self.main_page.locators.DROP_AREA
        )

        new_value = self.main_page.get_ingredient_counter_value()
        assert new_value == initial_value + 1, f"Счётчик не увеличился. "    

    @allure.story("Проверка текстов модального окна при оформлении заказа")
    def test_order_placement(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser) 


        login_page.open()
        login_page.enter_email(self.user['email'])
        login_page.enter_password(self.user['password'])
        login_page.click_login_button()


        main_page.click_order_button()
        main_page.wait_for_order_modal()



        modal_title = main_page.get_modal_title()
        assert modal_title.lower() == "идентификатор заказа", \
            f"Неверный заголовок модального окна: {modal_title}"

        order_message = main_page.get_order_message()
        assert "ваш заказ начали готовить" in order_message.lower(), \
            f"Отсутствует ожидаемое сообщение: {order_message}"
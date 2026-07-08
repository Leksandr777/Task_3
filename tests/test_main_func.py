import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.Ingredient_modal_locators import IngredientModalLocators
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from helpers import create_user, delete_user

@allure.feature("Функционал главной страницы и конструктора")
class TestMainFunc:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.login_page = LoginPage(browser)
        self.user = create_user() 

        yield
        delete_user(self.user) 

    @allure.story("Переход на ленту заказов (feed)")
    def test_step_to_feed(self, browser):
        self.main_page.open()
        self.main_page.go_to_feed()

        assert "/feed" in self.main_page.driver.current_url

    @allure.story("Переход в конструктор бургеров")
    def test_step_to_constructor(self, browser):
        main_page = MainPage(browser)
        
        main_page.open()
        main_page.go_to_constructor()

        header = main_page.wait_until_visible(MainPageLocators.CONSTRUCTOR_HEADER)
        assert header.is_displayed(), "Заголовок конструктора не отображается"

        assert main_page.base_url in main_page.driver.current_url, \
            f"Ожидался URL {main_page.base_url}, но был {main_page.driver.current_url}"

    @allure.story("Открытие модального окна ингредиента")
    def test_ingredient_modal(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_constructor()

        main_page.open_ingredient_modal(MainPageLocators.FIRST_SAUCE_INGREDIENT)


        modal_title_el = main_page.wait_until_visible(IngredientModalLocators.MODAL_TITLE)
        assert modal_title_el.text == "Детали ингредиента", "Неверный заголовок модального окна"


        assert "/ingredient/" in main_page.driver.current_url, "URL не изменился после открытия модального окна"

    @allure.story("Увеличение счётчика ингредиентов при драге")
    def test_ingredient_counter_increase(self, browser):
        main_page = MainPage(browser)
        

        main_page.open()
 
        ingredient_to_drag = browser.find_element(*MainPageLocators.FIRST_SAUCE_INGREDIENT)
        drop_area = browser.find_element(*MainPageLocators.DROP_AREA)
        
        initial_counter = browser.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        initial_value = int(initial_counter.text)
        
        main_page.drag_and_drop_ingredient(
            MainPageLocators.FIRST_SAUCE_INGREDIENT,
            MainPageLocators.DROP_AREA
        )
        
        new_counter = browser.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        assert int(new_counter.text) == initial_value + 1, \
            f"Счётчик не увеличился. Было {initial_value}, стало {new_counter.text}"

    @allure.story("Оформление заказа и проверка модального окна")
    def test_order_placement(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)  # если ещё не инициализирован в setup


        login_page.open()
        login_page.enter_email(self.user['email'])
        login_page.enter_password(self.user['password'])
        login_page.click_login_button()


        main_page.click_order_button()
        main_page.wait_for_order_modal()


        order_id = main_page.get_order_id()
        assert order_id > 0, "Номер заказа должен быть положительным числом"

        modal_title = main_page.get_modal_title()
        assert modal_title.lower() == "идентификатор заказа", \
            f"Неверный заголовок модального окна: {modal_title}"

        order_message = main_page.get_order_message()
        assert "ваш заказ начали готовить" in order_message.lower(), \
            f"Отсутствует ожидаемое сообщение: {order_message}"
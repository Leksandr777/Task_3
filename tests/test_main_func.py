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
        main_page = MainPage(browser)
        
        main_page.open()
        main_page.go_to_constructor()

        assert main_page.wait_until_visible(MainPageLocators.CONSTRUCTOR_HEADER).is_displayed()

        assert self.main_page.is_url_contains(self.main_page.base_url)

    @allure.story("Открытие модального окна ингредиента")
    def test_ingredient_modal(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_constructor()

        main_page.open_ingredient_modal(MainPageLocators.FIRST_SAUCE_INGREDIENT)


        modal_title_el = main_page.wait_until_visible(IngredientModalLocators.MODAL_TITLE)
        assert modal_title_el.text == "Детали ингредиента", "Неверный заголовок модального окна"


        assert self.main_page.is_url_contains(INGREDIENT_URL), "URL не изменился после открытия модального окна"


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
import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
#from locators.main_page_locators import MainPageLocators
from helpers import create_user, delete_user
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Авторизация")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser)
        self.main_page = MainPage(browser)
        self.user = create_user()  

        yield
        delete_user(self.user)  

    @allure.story("Успешная авторизация пользователя")
    def test_successful_login(self):

        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()
        
        assert self.login_page.is_user_logged_in(), "Пользователь не авторизован"

    @allure.story("Переход в историю заказов после авторизации")
    def test_step_to_order_history(self):

        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()
        self.main_page.waiting_for_user_logged_in()
        self.main_page.go_to_personal_cabinet()
        self.main_page.go_to_order_history()
        assert "/account/order-history" in self.login_page.driver.current_url

    @allure.story("Выход из аккаунта (logout)")
    def test_logout(self):
        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()
        
        # Ждем появления кнопки личного кабинета
        self.main_page.waiting_for_user_logged_in()
        self.main_page.go_to_personal_cabinet()       
        self.main_page.logout()
        expected_url = "https://qa-stellarburgers.education-services.ru/login"
        WebDriverWait(self.login_page.driver, 10).until(
            EC.url_to_be(expected_url)
        )
        
        assert self.login_page.driver.current_url == expected_url, \
            f"Ожидался URL: {expected_url}, но получен: {self.login_page.driver.current_url}"
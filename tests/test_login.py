import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
#from locators.main_page_locators import MainPageLocators
from helpers import create_user, delete_user
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import LOGIN_PAGE_URL, ORDER_HISTORY_URL

@allure.feature("Авторизация")
@pytest.mark.usefixtures("setup_pages_and_user")
class TestLogin:



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
        assert self.login_page.is_url_contains(ORDER_HISTORY_URL)


    @allure.story("Выход из аккаунта (logout)")
    def test_logout(self):
        self.login_page.open()
        self.login_page.enter_email(self.user['email'])
        self.login_page.enter_password(self.user['password'])
        self.login_page.click_login_button()
        

        self.main_page.waiting_for_user_logged_in()
        self.main_page.go_to_personal_cabinet()       
        self.main_page.logout()
        expected_url = LOGIN_PAGE_URL
        self.login_page.wait_url_to_be(expected_url, timeout=10)
        
        current_url = self.login_page.get_current_url()
        assert current_url == expected_url

import allure
import pytest
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.reset_password_page import ResetPasswordPage
from pages.main_page import MainPage
from helpers import create_user, delete_user
from constant import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL

@allure.feature("Восстановление пароля")
@pytest.mark.usefixtures("setup_pages_and_user")
class TestPasswordReset:



    @allure.story("Переход по ссылке Восстановление пароля")
    def test_reset_password_link(self, browser):

        self.login_page.open()
        self.login_page.click_recovery_password_link()

        assert self.login_page.is_url_contains(FORGOT_PASSWORD_URL), "Не перешли на страницу восстановления"


    @allure.story("Отправка email для сброса пароля")
    def test_email_reset_success(self):

        self.login_page.open()
        self.login_page.click_recovery_password_link()

        self.password_recovery_page.enter_email(self.user['email'])
        self.password_recovery_page.click_recovery_button()

        assert self.login_page.is_url_contains(RESET_PASSWORD_URL)

    @allure.story("Переключение переключателя видимости парооля")
    def test_show_password(self):

        self.login_page.open()
        self.login_page.click_recovery_password_link()
        
        self.password_recovery_page.enter_email(self.user['email'])
        self.password_recovery_page.click_recovery_button() 

        self.reset_password_page.wait_for_page_load()      

        test_password = "qwerty123"
        
        self.reset_password_page.enter_password(test_password)

        initial_type = self.reset_password_page.get_password_input_type()
        assert initial_type == "password", f"Ожидался type='password', но было: {initial_type}"

        self.reset_password_page.click_show_password()    

        new_type = self.reset_password_page.get_password_input_type()
        displayed_password = self.reset_password_page.get_password_input_value()

        assert new_type == "text", f"Ожидался type='text', но было: {new_type}"
        assert displayed_password == test_password, f"Пароль не совпал."
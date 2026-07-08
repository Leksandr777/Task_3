import allure
import pytest
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.reset_password_page import ResetPasswordPage
from helpers import create_user, delete_user

@allure.feature("Восстановление пароля")
class TestPasswordReset:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser)
        self.user = create_user()
        
        yield
        delete_user(self.user)

    @allure.story("Переход по ссылке Восстановление пароля")
    def test_reset_password_link(self, browser):
        login_page = LoginPage(browser)
        login_page.open()

        login_page.click_recovery_password_link()

        assert "forgot-password" in browser.current_url

    @allure.story("Отправка email для сброса пароля")
    def test_email_reset_success(self):

        self.login_page.open()

        self.login_page.click_recovery_password_link()

        recovery_page = PasswordRecoveryPage(self.login_page.driver)
        recovery_page.enter_email(self.user['email'])
        
        recovery_page.click_recovery_button()

        assert "/reset-password" in self.login_page.driver.current_url, \
            f"Ожидался переход на /reset-password"

    @allure.story("Переключение переключателя видимости парооля")
    def test_show_password(self):

        self.login_page.open()
        self.login_page.click_recovery_password_link()

        recovery_page = PasswordRecoveryPage(self.login_page.driver)
        recovery_page.enter_email(self.user['email'])
        recovery_page.click_recovery_button() 

        reset_page = ResetPasswordPage(self.login_page.driver)
        reset_page.wait_for_page_load()      

        test_password = "qwerty123"
        password_field = reset_page.enter_password(test_password)

        initial_type = password_field.get_attribute("type")
        assert initial_type == "password", f"Ожидался type='password', но было: {initial_type}"

        reset_page.click_show_password()    

        updated_field = self.login_page.driver.find_element(*reset_page.locators.PASSWORD_INPUT)
        
        new_type = updated_field.get_attribute("type")
        displayed_password = updated_field.get_attribute("value")

        assert new_type == "text", f"Ожидался type='text'"
        assert displayed_password == test_password, f"Пароль не совпал"

from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PAGE_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".BurgerConstructor_basket__container__2fUl3 button")
    LOGIN_WITH_CRED_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[contains(@href, '/forgot-password')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Оформить заказ')]")


from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:

    RECOVERY_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    RECOVERY_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".show-password-button")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PAGE_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    RECOVERY_BUTTON = (By.XPATH,"//button[text()='Восстановить']")

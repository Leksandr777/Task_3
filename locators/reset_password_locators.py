from selenium.webdriver.common.by import By

class ResetPasswordLocators:
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']")
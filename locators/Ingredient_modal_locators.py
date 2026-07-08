from selenium.webdriver.common.by import By

class IngredientModalLocators:
    MODAL_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified') and contains(text(), 'Детали ингредиента')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    MODAL_BACKDROP = (By.CSS_SELECTOR, ".modal-backdrop")  
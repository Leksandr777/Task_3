from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_CABINET_LINK = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@class, 'Account_link__2ETsJ') and contains(@href, '/account/order-history') and text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Войти']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента Заказов']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Соберите бургер']")
    INGREDIENTS_LIST = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")
    FIRST_SAUCE_INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/691577430cc94f001a65b862') and contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")

    FIRST_BUN_INGREDIENT = (By.XPATH,"//ul[contains(@class, 'BurgerIngredients_ingredients__list__2A-mT')]/a[1]")    
    DROP_AREA = (By.CSS_SELECTOR, ".BurgerConstructor_basket__listItem__aWMu1")
    INGREDIENT_COUNTER =  (By.XPATH,"//a[contains(@href, '/ingredient/691577430cc94f001a65b862')]//div[contains(@class, 'counter_counter__ZNLkj')]//p[@class='counter_counter__num__3nue1']")
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    MODAL_TITLE = (By.XPATH, "//p[contains(text(), 'идентификатор заказа')]")
    ORDER_MESSAGE = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary__1O7Bx') and contains(text(), 'Оформить заказ')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]") 
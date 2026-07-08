from selenium.webdriver.common.by import By

class  OrderFeedLocators:

# В OrderFeedLocators:
    ORDERS_LIST = (By.CLASS_NAME, 'OrderFeed_list__OLh59')
    FIRST_ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r')]/a[contains(@class, 'OrderHistory_link__1iNby')]")
    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default') and starts-with(., '#')]")
    COMPOSITION_HEADER = (By.XPATH, "//p[contains(@class, 'text_type_main-medium') and text()='Состав']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, '.Modal_orderBox__1xWdi .Modal_closeButton' )
    ORDER_NUMBER_IN_LIST = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
    ORDER_STATUS = (By.XPATH, ".//p[contains(@class, 'OrderHistory_visible__19YMB')]")
    BURGER_NAME = (By.XPATH, ".//h2[contains(@class, 'text_type_main-medium')]")
    ORDER_BY_NUMBER = (By.XPATH, "//p[text()='{number}']/ancestor::li[contains(@class, 'OrderHistory_listItem__2x95r')]")

    FIRST_BUN_INGREDIENT = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a")
    TOTAL_ORDERS_COUNTER = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large")

    ORDERS_IN_WORK = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem li.text.text_type_digits-default")
    NO_ORDERS_MESSAGE = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text.text_type_main-small")

    TODAY_ORDERS_COUNTER = ( By.CSS_SELECTOR, "div > p:nth-child(2).OrderFeed_number__2MbrQ.text.text_type_digits-large")
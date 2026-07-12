import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from helpers import create_user, delete_user

@pytest.fixture(params=["chrome"])#, "firefox"
def browser(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    
    yield driver
    driver.quit()

def pytest_runtest_teardown(item, nextitem):
    time.sleep(3)

@pytest.fixture(autouse=True)
def setup_pages_and_user(request, browser):


    login_page = LoginPage(browser)
    main_page = MainPage(browser)
    order_feed_page = OrderFeedPage(browser) 
    user = create_user()

    request.cls.login_page = login_page
    request.cls.main_page = main_page
    request.cls.user = user
    request.cls.order_feed_page = order_feed_page
    request.cls.driver = browser

    yield

    delete_user(user)
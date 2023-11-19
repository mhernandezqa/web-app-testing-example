import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from data.test_data import TestData
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time

test_data = TestData()

URL = test_data.url
USERNAME = test_data.username
PASSWORD = test_data.password

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

@pytest.fixture(scope="class")
def login_logout(request, chrome_driver_init):
    driver = request.cls.driver
    driver.get(URL)
    driver.maximize_window()
    base_page = BasePage(driver)
    username_input = base_page.text_input_by_placeholder(placeholder="Username")
    print("Username input:", username_input)  # Add this line
    username_input.send_keys(USERNAME)
    password_input = base_page.text_input_by_placeholder(placeholder="Password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)

@pytest.fixture(scope="function")
def check_intentory_url(request, login_logout):
    inventory_url = f"{URL}inventory.html"
    driver = request.cls.driver
    current_url = driver.current_url
    if current_url != inventory_url:
        driver.get(inventory_url)

@pytest.fixture(scope="function")
def check_cart_url(request, login_logout):
    cart_url = f"{URL}cart.html"
    driver = request.cls.driver
    current_url = driver.current_url
    if current_url != cart_url:
        driver.get(cart_url)

@pytest.fixture(scope="function")
def check_checkout_step_one_url(request, login_logout):
    checkout_step_one_url = f"{URL}checkout-step-one.html"
    driver = request.cls.driver
    current_url = driver.current_url
    if current_url != checkout_step_one_url:
        driver.get(checkout_step_one_url)
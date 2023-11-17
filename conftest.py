import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
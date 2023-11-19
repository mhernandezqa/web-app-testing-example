from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CheckoutStepTwoPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
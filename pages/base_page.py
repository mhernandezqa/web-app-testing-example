from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    def text_input_by_placeholder(self, placeholder: str):
        locator = (By.XPATH, f"//input[contains(@placeholder,'{placeholder}')]")
        text_input = self.wait.until(EC.visibility_of_element_located(locator))
        return text_input
        
    def add_to_cart_button(self, item_name: str):
        locator = (By.XPATH, f"//div[contains(text(),'{item_name}')]/ancestor::div[contains(@class,'inventory_item')]/descendant::button[contains(text(),'Add to cart')]")
        button = self.wait.until(EC.element_to_be_clickable(locator))
        return button
    
    def remove_button(self, item_name: str):
        locator = (By.XPATH, f"//div[contains(text(),'{item_name}')]/ancestor::div[contains(@class,'inventory_item')]/descendant::button[contains(text(),'Remove')]")
        button = self.wait.until(EC.element_to_be_clickable(locator))
        return button
    
    def button(self, button_name: str):
        locator = (By.XPATH, f"//button[contains(text(),'{button_name}')]")
        button = self.wait.until(EC.element_to_be_clickable(locator))
        return button
    
    def input_by_name(self, name: str):
        locator = (By.XPATH, f"//input[contains(@name,'{name}')]")
        button = self.wait.until(EC.element_to_be_clickable(locator))
        return button


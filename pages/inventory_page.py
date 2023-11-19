from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
    
    def item(self, item_name: str):
        locator = (By.XPATH, f"//div[contains(text(),'{item_name}')]")
        item = self.wait.until(EC.visibility_of_element_located(locator))
        return item
    

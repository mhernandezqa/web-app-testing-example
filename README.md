# E-Shop Web App Testing Example

# A fully functional EXAMPLE project written in Python showing how to perform UI tests on web applications with the Selenium library and the Pytest test framwework.

This project uses as reference a web application built for testing pruposes: https://www.saucedemo.com/. This project shows how to do the following:

* Establish a base directory structure for organizing your test files, reusable test data, utilities and web pages locators.

```

webapptestingtemplate/
│
├── tests/
│   ├── __init__.py
│   ├── test_base.py
│   └── ...
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── ...
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── helpers.py
│   └── ...
│
├── data/
│   ├── __init__.py
│   ├── test_data.py
│   └── ...
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── run_tests.py

```

* Create the starting page file, such as base_page.py, which contains the skeleton of the web page on top of which you should keep building more specific section structures.

```
# Base page code

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

```

```
# This is an example on how the Inventory page file inheritates the base structure from the Base page file to keep adding more page-specific locators.

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
```
* Create the starting test file, such as test_base.py, which contains the essential actions that must be executed before each separated test: initialize the webdriver and login.

* Create the conftest.py file, which contains the essential pytest fixtures to perform the tests succesfully.
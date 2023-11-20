# E-Shop Web App Testing Example

# A fully functional EXAMPLE project written in Python showing how to perform UI tests on web applications with the Selenium library and the Pytest test framework.

This project references a web application built for testing purposes: https://www.saucedemo.com/. This project shows how to do the following:

* Establish a base directory structure for organizing test files, reusable test data, utilities, and web page locators.

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

* Create the starting page file, such as base_page.py, which contains the skeleton of the web page on top of which you should keep building more section-specific structures.

```
# base_page.py code

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
# This is an example of how the inventory_page.py file inherits the base structure from the Base page file to keep adding more page-specific locators.

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
* Create the starting test file, such as test_base.py, which contains the essential actions to execute before each separate test: initialize the web driver and log in.

```
# test_base.py file

import pytest


@pytest.mark.usefixtures("chrome_driver_init")
@pytest.mark.usefixtures("login_logout")
class BasicTest:
    
    pass

```
```
# This is an example of how in the test_inventory.py the TestInventoryFunctionalityfile class inherits the base structure from the test_base.py BasicTest to keep adding more test-case-specific functions.

from .test_base import BasicTest
from pages.inventory_page import InventoryPage
import pytest

@pytest.mark.usefixtures("check_intentory_url")
class TestInventoryFunctionality(BasicTest):

    @pytest.fixture(scope="class")
    def inventory_page(self):
        return InventoryPage(self.driver)

    @pytest.mark.parametrize("name", ["Sauce Labs Backpack"])
    def test_item_link(self, name, inventory_page, request):
        item = inventory_page.item(item_name=name)
        item.click()
        driver = request.cls.driver
        current_url = driver.current_url
        assert "/inventory-item.html?id=" in current_url

```
* Create the conftest.py file, which contains the essential pytest fixtures to perform the tests successfully.

```

# Sneak peek in the conftest.py file that shows the pytest fixture chrome_driver_init, used for initializing the webdriver before each test.

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()

```
## How to use this example project:

1. clone this project
2. Install the required libraries, modules and packages. Run this command within the project's root directory.
```
pip install -r requirements.txt
```
3. (Optional) Run all the tests in the "tests/" directory. Run this command within the project's root directory.
```
pytest tests/
```
[![Watch the video](https://img.youtube.com/vi/b5fkUCeJwHk/hqdefault.jpg)](https://youtu.be/b5fkUCeJwHk)

[<img src="https://img.youtube.com/vi/b5fkUCeJwHk/hqdefault.jpg" width="600" height="300"
/>](https://www.youtube.com/embed/b5fkUCeJwHk)

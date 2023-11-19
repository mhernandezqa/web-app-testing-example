# E-Shop Web App Testing Example

# A fully functional EXAMPLE project written in Python showing how to perform UI tests on web applications with the Selenium library and the Pytest test framwework.

This project uses as reference a web application built for testing pruposes: https://www.saucedemo.com/. This project shows how to do the following:

* Establish a base directory structure for organizing your test files, reusable test data, utilities and web pages locators.

* Create the starting page file, such as base_page.py, which contains the skeleton of the web page on top of which you should keep building more specific section structures.

* Create the starting test file, such as test_base.py, which contains the essential actions that must be executed before each separated test: initialize the webdriver and login.

* Create the conftest.py file, which contains the essential pytest fixtures to perform the tests succesfully.

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

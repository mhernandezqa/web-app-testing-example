import os

class TestData:

    url = "https://www.saucedemo.com/"
    username = os.environ.get("DEMO_USERNAME")
    password = os.environ.get("DEMO_PASSWORD")
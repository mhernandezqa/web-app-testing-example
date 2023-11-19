from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage



def fill_text_input(text):
    base_page = BasePage()
    base_page.text_input_by_placeholder(text=text).send_keys(text)
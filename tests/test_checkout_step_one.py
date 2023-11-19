from .test_base import BasicTest
from pages.checkout_step_one_page import CheckoutStepOnePage
import pytest
import time

@pytest.mark.usefixtures("check_checkout_step_one_url")
class TestCheckoutStepOneFunctionality(BasicTest):

    @pytest.fixture(scope="class")
    def checkout_step_one_page(self):
        return CheckoutStepOnePage(self.driver)
    
    @pytest.mark.parametrize("placeholder, text", [("First Name", "John"), ("Last Name","Doe"), ("Zip/Postal Code","32304")])
    def test_form(self, placeholder, text, checkout_step_one_page):
        first_name_input = checkout_step_one_page.text_input_by_placeholder(placeholder=placeholder)
        first_name_input.send_keys(text)
        first_name_input_attribute = checkout_step_one_page.text_input_by_placeholder(placeholder=placeholder).get_attribute("value")
        assert text in first_name_input_attribute

    @pytest.mark.parametrize("name, path", [("Continue", "checkout-step-two.html")])
    def test_continue_button(self, name, path, checkout_step_one_page, request):
        continue_button = checkout_step_one_page.input_by_value(value=name)
        continue_button.click()
        driver = request.cls.driver
        current_url = driver.current_url
        assert path in current_url

    @pytest.mark.parametrize("name, path", [("Cancel","cart.html")])
    def test_cancel_button(self, name, path, checkout_step_one_page, request):
        continue_button = checkout_step_one_page.button(button_name=name)
        continue_button.click()
        driver = request.cls.driver
        current_url = driver.current_url
        assert path in current_url
    


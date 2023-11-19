from .test_base import BasicTest
from pages.checkout_step_two_page import CheckoutStepTwoPage
import pytest

@pytest.mark.usefixtures("check_checkout_step_two_url")
class TestCheckoutStepOneFunctionality(BasicTest):

    @pytest.fixture(scope="class")
    def checkout_step_two_page(self):
        return CheckoutStepTwoPage(self.driver)
    
    @pytest.mark.parametrize("name, path", [("Finish", "checkout-complete.html")])
    def test_finish_button(self, name, path, checkout_step_two_page, request):
        finish_button = checkout_step_two_page.button(button_name=name)
        finish_button.click()
        driver = request.cls.driver
        current_url = driver.current_url
        assert path in current_url

    @pytest.mark.parametrize("name, path", [("Cancel","inventory.html")])
    def test_cancel_button(self, name, path, checkout_step_two_page, request):
        continue_button = checkout_step_two_page.button(button_name=name)
        continue_button.click()
        driver = request.cls.driver
        current_url = driver.current_url
        assert path in current_url
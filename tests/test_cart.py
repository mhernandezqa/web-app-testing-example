from .test_base import BasicTest
from pages.cart_page import CartPage
import pytest
import time

@pytest.mark.usefixtures("check_cart_url")
class TestCartFunctionality(BasicTest):

    @pytest.fixture(scope="class")
    def cart_page(self):
        return CartPage(self.driver)
    
    @pytest.mark.parametrize("name, path", [("Checkout", "checkout-step-one.html"), ("Continue Shopping","inventory.html")])
    def test_buttons(self, name, path, cart_page, request):
        button = cart_page.button(button_name=name)
        button.click()
        driver = request.cls.driver
        current_url = driver.current_url
        assert path in current_url
    

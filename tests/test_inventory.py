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
    
    @pytest.mark.parametrize("name", ["Sauce Labs Backpack"])
    def test_add_to_cart_button(self, name, inventory_page):
        button = inventory_page.add_to_cart_button(item_name=name)
        button.click()
        assert inventory_page.remove_button(item_name=name)

    @pytest.mark.parametrize("name", ["Sauce Labs Backpack"])
    def test_remove_button(self, name, inventory_page):
        button = inventory_page.remove_button(item_name=name)
        button.click()
        assert inventory_page.add_to_cart_button(item_name=name)
    
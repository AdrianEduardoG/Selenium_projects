from pages.InventoryPage import InventoryPage
from utils.webdriver import get_chrome_driver
from pages.LoginPage import LoginPage
import pytest

@pytest.fixture
def driver():
    driver = get_chrome_driver()
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    yield driver

    driver.quit()

def test_add_cart(driver):
    inventory_page = InventoryPage(driver)
    buttons = inventory_page.add_cart()
    cart_qty = inventory_page.cart_button_mount()

    assert int(cart_qty.text) == buttons



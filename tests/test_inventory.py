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

def test_menu_button(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.element_titles()

def test_add_to_cart(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart(5)

def test_add_all_to_cart(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.add_all_to_cart()

def test_filter_by_value(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.filter("az")
    inventory_page.filter("za")
    inventory_page.filter("lohi")
    inventory_page.filter("hilo")

def test_cart(driver):
    inventory_page = InventoryPage(driver)
    inventory_page.cart()

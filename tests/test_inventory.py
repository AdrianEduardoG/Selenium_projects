from pages.InventoryPage import InventoryPage
from utils.webdriver import get_chrome_driver
from pages.LoginPage import LoginPage
import pytest
import time

@pytest.fixture
def driver():
    driver = get_chrome_driver()
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    yield driver

    # driver.quit()

@pytest.fixture
def inventory_page(driver):
    inventory_page = InventoryPage(driver)
    
    yield inventory_page

def test_add_to_cart_last_accessory(inventory_page):
    inventory_page.add_to_cart(5)
    qty = int(inventory_page.qty_cart_element())

    assert qty == 1

def test_add_to_cart_first_accessory(inventory_page):
    inventory_page.add_to_cart(0)
    qty = int(inventory_page.qty_cart_element())

    assert qty == 1

def test_add_all_to_cart(inventory_page):
    inventory_page.add_all_to_cart()
    qty = int(inventory_page.qty_cart_element())

    assert qty == 6

def test_delete_one_accessory_from_the_cart(inventory_page):
    inventory_page.add_all_to_cart()
    inventory_page.add_to_cart(0)
    qty = int(inventory_page.qty_cart_element())

    assert qty == 5

def test_delete_all_accessories_from_the_cart(inventory_page):
    inventory_page.add_all_to_cart()
    inventory_page.add_all_to_cart()
    
    try:
        qty = inventory_page.qty_cart_element()
    except:
        assert True

def test_redirected_to_selected_accessory(inventory_page):
    inventory_page.click_element_title("Sauce Labs Backpack")
    # url = inventory_page.get_url()
    title = inventory_page.element_title()

    # assert url == "https://www.saucedemo.com/inventory-item.html?id=4"
    assert title == "Sauce Labs Backpack"

def test_redirected_to_every_accessory(inventory_page):
    '''
    titles was added in a list comprehension to save all the visible titles and avoiding them to be
    eliminated when being redirected to another page
    '''
    titles = [title.text for title in inventory_page.get_link_titles_text()]

    PASSED = 0
    ACTUAL = 0
    for title in titles:
        inventory_page.click_selected_element_title(PASSED)
        actual_title = inventory_page.element_title()

        if (title == actual_title):
            PASSED += 1
        inventory_page.click_back_to_inventory()
        ACTUAL += 1
    
    assert PASSED == 6

def test_clicking_about_in_burger_menu(inventory_page):
    inventory_page.menu_about()

    assert inventory_page.get_url() == "https://saucelabs.com/"

def test_clicking_logout_in_burger_menu(inventory_page):
    inventory_page.menu_log_out()

    assert inventory_page.get_url() == "https://www.saucedemo.com/"

def test_filter_z_to_a(inventory_page):
    inventory_page.filter("za")
    titles = [title.text for title in inventory_page.get_link_titles_text()]

    assert titles[0] == "Test.allTheThings() T-Shirt (Red)"

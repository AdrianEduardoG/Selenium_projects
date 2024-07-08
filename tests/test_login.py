from pages.LoginPage import LoginPage
from utils.webdriver import get_chrome_driver
from selenium.common.exceptions import NoSuchElementException
import pytest

@pytest.fixture
def driver():
    driver = get_chrome_driver()

    yield driver

    driver.quit()

#TC001
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "https://www.saucedemo.com/inventory.html" in login_page.retrieve_url()
    
#TC002
def test_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "password")

    assert driver.current_url == 'https://www.saucedemo.com/'

#TC003
def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "")
    error = login_page.error_message()

    assert "Password is required" in error.text

#TC004
def test_error_color(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "")

    error = login_page.error_color()

    assert "rgba(226, 35, 26, 1)" == error

#TC005
def test_error_closed(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "")
    
    login_page.click_error_button()

    try:
        login_page.deleted_element()
        pytest.fail("Element was not deleted")

    except NoSuchElementException:
            assert True

#TC006        
def test_redirect_to_login_form(driver):
    login_page = LoginPage(driver)
    login_page.custom_load("https://www.saucedemo.com/inventory.html")


    assert login_page.retrieve_url() == "https://www.saucedemo.com/"
    
#TC007
def test_redirect_to_login_form_error(driver):
    login_page = LoginPage(driver)
    login_page.custom_load("https://www.saucedemo.com/inventory.html")

    error = login_page.error_message()

    assert "You can only access '/inventory.html' when you are logged in" in error.text

#TC008 
def test_wrong_username(driver):
    login_page = LoginPage(driver)
    login_page.login("user", "secret_sauce")

    error = login_page.error_message()

    assert "Username and password do not match any user in this service" in error.text

#TC009
def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.login("", "secret_sauce")
    
    error = login_page.error_message()

    assert "Username is required" in error.text








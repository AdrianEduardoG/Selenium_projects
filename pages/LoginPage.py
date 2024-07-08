from selenium.webdriver.common.by import By
from .BasePage import BasePage
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC 

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
        self.USER_NAME_TYPE         = By.ID
        self.PASSWORD_TYPE          = By.ID
        self.SUBMIT_TYPE            = By.ID
        self.ERROR_MESSAGE_TYPE     = By.CLASS_NAME
        self.ERROR_BUTTON_TYPE      = By.CLASS_NAME
        self.ERROR_CONTENT_TYPE     = By.XPATH
        self.USER_NAME_ID           = "user-name"
        self.PASSWORD_ID            = "password"
        self.SUBMIT_TYPE_ID         = "login-button"
        self.ERROR_MESSAGE_CLASS    = "error-message-container"
        self.ERROR_BUTTON_CLASS     = "error-button"
        self.ERROR_CONTENT_XPATH    = "//h3"

    def load(self):
        self.open(self.url)

    def custom_load(self, url):
        self.open(url)

    def retrieve_url(self):
        return self.get_url()

    def username(self, username):
        self.type_text(self.USER_NAME_TYPE, self.USER_NAME_ID, username)
    
    def password(self, password):
        self.type_text(self.PASSWORD_TYPE, self.PASSWORD_ID, password)

    def click_submit(self):
        self.click(self.SUBMIT_TYPE, self.SUBMIT_TYPE_ID)

    def error_message(self):
        return self.find_element(self.ERROR_MESSAGE_TYPE, self.ERROR_MESSAGE_CLASS)
    
    def error_color(self):
        error  = self.find_element(self.ERROR_MESSAGE_TYPE, self.ERROR_MESSAGE_CLASS)
        return error.value_of_css_property('background-color')

    def click_error_button(self):
        self.find_element(self.ERROR_BUTTON_TYPE, self.ERROR_BUTTON_CLASS).click()
    
    def deleted_element(self):
        return self.find_element(self.ERROR_CONTENT_TYPE, self.ERROR_CONTENT_XPATH)
        
    def login(self, username, password):
        self.load()
        self.username(username)
        self.password(password)
        self.click_submit()
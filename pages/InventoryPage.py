from selenium.webdriver.common.by import By
from .BasePage import BasePage
import time

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        # self.ADD_TO_CART_BUTTON = By.XPATH
        # self.ITEM_TITLE         = By.LINK_TEXT
        # self.SELECT_FILTER_BOX  = By.CLASS_NAME
        # self.CART_BUTTON        = By.CLASS_NAME
        # self.LEFT_MENU          = By.ID

        # self.ADD_TO_CARD_BUTTON_CLASS   = "//div[@class='inventory_list']//button[@class='btn_primary']"
        # self.SELECT_FILTER_CLASS        = "product_sort_container"
        # self.CART_BUTTON_CLASS          = "shopping_cart_link" 
        # self.LEFT_MENU_ID               = "react-burger-menu-btn"

        self.ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='inventory_list']//button")
        self.ITEM_TITLE         = By.LINK_TEXT
        self.SELECT_FILTER_BOX  = (By.CLASS_NAME, "product_sort_container")
        self.CART_BUTTON_CLASS  = (By.CLASS_NAME, "shopping_cart_link")
        self.LEFT_MENU          = (By.ID, "react-burger-menu-btn")

    def add_cart(self):
        buttons = self.find_elements(self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1])

        for button in buttons:
            self.click_by_driver(button)

        return len(buttons)
    
    def cart_button_mount(self):
        return self.find_element(self.CART_BUTTON_CLASS[0], self.CART_BUTTON_CLASS[1])
    
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

        self.LEFT_MENU          = (By.ID, "react-burger-menu-btn")
        self.MENU_ABOUT         = (By.ID, "about_sidebar_link")
        self.ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='inventory_list']//button")
        self.ITEM_TITLE         = By.LINK_TEXT
        self.SELECT_FILTER_BOX  = (By.CLASS_NAME, "product_sort_container")
        self.CART_BUTTON_CLASS  = (By.CLASS_NAME, "shopping_cart_link")

    def menu_button(self):
        self.click(self.LEFT_MENU[0], self.LEFT_MENU[1])

    def menu_about(self):
        self.menu_button()
        self.click(self.MENU_ABOUT[0], self.MENU_ABOUT[1])

    
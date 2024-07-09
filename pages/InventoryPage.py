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
        self.MENU_LOGOUT        = (By.ID, "logout_sidebar_link")
        self.MENU_CLOSE         = (By.ID, "react-burger-cross-btn")    
        # self.ITEM_TITLE         = (By.XPATH, "//div[@class='inventory_item_label']//a")
        self.ELEMENT_TITLE      = By.LINK_TEXT
        self.ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='inventory_list']//button")
        self.SELECT_FILTER_BOX  = (By.CLASS_NAME, "product_sort_container")
        self.CART_BUTTON_CLASS  = (By.CLASS_NAME, "shopping_cart_link")

    def menu_button(self):
        self.click_by_script(self.LEFT_MENU[0], self.LEFT_MENU[1])

    def menu_about(self):
        self.menu_button()
        self.click_by_script(self.MENU_ABOUT[0], self.MENU_ABOUT[1])

    def menu_log_out(self):
        self.menu_button()
        self.click_by_script(self.MENU_LOGOUT[0],self.MENU_LOGOUT[1])

    def menu_close(self):
        self.menu_button()
        self.click_by_script(self.MENU_CLOSE[0],self.MENU_CLOSE[1])

    def element_titles(self, title):
        self.click(self.ITEM_TITLE, title)

    def add_to_cart(self, element_selected):
        self.click_selected_buttons(self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1], element_selected)

    def add_all_to_cart(self):
        self.click_all_buttons(self.ADD_TO_CART_BUTTON[0], self.ADD_TO_CART_BUTTON[1])

    def filter(self, value):
        self.select_by_value(self.SELECT_FILTER_BOX[0], self.SELECT_FILTER_BOX[1], value)

    def cart(self):
        self.click(self.CART_BUTTON_CLASS[0], self.CART_BUTTON_CLASS[1])
    
    


    
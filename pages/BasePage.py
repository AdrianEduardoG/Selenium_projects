from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, by, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
    
    def find_elements(self, by, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by, selector)))
    
    def click(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, selector))).click()

    def click_by_script(self, by, selector):
        element = self.find_element(by, selector)
        self.driver.execute_script("arguments[0].click();", element)

    def click_selected_buttons(self, by, selector, element_selected):
        element = self.find_elements(by, selector)
        element[element_selected].click()

    def click_all_buttons(self, by, selector):
        elements = self.find_elements(by, selector)
        for element in elements:
            element.click()

    def select_by_value(self, by, selector, value):
        element = self.find_element(by, selector)
        select = Select(element)
        select.select_by_value(value)

    def type_text(self, by, selector, text):
        element = self.driver.find_element(by, selector)
        element.clear()
        element.send_keys(text)
    
    def get_url(self):
        return self.driver.current_url


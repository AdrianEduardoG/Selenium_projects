class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)
    
    def find_elements(self, by, selector):
        return self.driver.find_elements(by, selector)
    
    def click(self, by, selector):
        element  = self.driver.find_element(by, selector)
        element.click()

    def click_by_driver(self, driver):
        driver.click()

    def type_text(self, by, selector, text):
        element = self.driver.find_element(by, selector)
        element.clear()
        element.send_keys(text)
    
    def get_url(self):
        return self.driver.current_url


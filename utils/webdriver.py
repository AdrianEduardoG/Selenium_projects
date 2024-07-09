from selenium import webdriver

def get_chrome_driver():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # return webdriver.Chrome(options=options)
    return webdriver.Chrome()
from selenium import webdriver

def get_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver

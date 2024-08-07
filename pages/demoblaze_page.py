from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoblazePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.demoblaze.com/"

    def go_to_home(self):
        self.driver.get(self.url)

    def select_product(self, index):
        self.find_element(By.XPATH, f'/html/body/div[5]/div/div[2]/div/div[{index}]/div/div/h4/a').click()

    def get_product_info(self):
        product_name = self.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/h2').text
        product_price_and_tax = self.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/h3').text
        product_price = product_price_and_tax.split()[0]
        return product_name, product_price

    def add_product_to_cart(self):
        self.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def go_to_cart(self):
        self.driver.get("https://www.demoblaze.com/cart.html#")

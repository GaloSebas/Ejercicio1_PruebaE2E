import unittest
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.webdriver import get_webdriver
from pages.demoblaze_page import DemoblazePage
from utils.helpers import set_variable, get_variable 

class TestAddProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_webdriver()
        cls.demoblaze = DemoblazePage(cls.driver)
        cls.demoblaze.go_to_home()

    def test_add_products(self):
        #Select the first product and obtain its info
        self.demoblaze.select_product(random.randint(1, 9))
        product_1_name, product_1_price = self.demoblaze.get_product_info()
        self.demoblaze.add_product_to_cart()
        #Select the second product and obtain its info
        self.demoblaze.go_to_home()
        self.demoblaze.select_product(random.randint(1, 9))
        product_2_name, product_2_price = self.demoblaze.get_product_info()
        self.demoblaze.add_product_to_cart()
        #Store the data obtained
        set_variable('PRODUCT_1_NAME', product_1_name)
        set_variable('PRODUCT_1_PRICE', product_1_price)
        set_variable('PRODUCT_2_NAME', product_2_name)
        set_variable('PRODUCT_2_PRICE', product_2_price)
        #Validate if the cart has the products (2)
        self.demoblaze.go_to_cart()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr")))
        rows = self.driver.find_elements(By.XPATH, "//table/tbody/tr")
        self.assertEqual(len(rows), 2, "The products are missing in the cart")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

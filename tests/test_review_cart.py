import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.webdriver import get_webdriver
from pages.demoblaze_page import DemoblazePage
from utils.helpers import get_variable, set_variable

class TestReviewCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_webdriver()
        cls.demoblaze = DemoblazePage(cls.driver)
        cls.demoblaze.go_to_cart()

    def test_review_cart(self):
        #Get all the variables needed for the test
        product_1_name = get_variable('PRODUCT_1_NAME')
        product_1_price = get_variable('PRODUCT_1_PRICE')
        product_2_name = get_variable('PRODUCT_2_NAME')
        product_2_price = get_variable('PRODUCT_2_PRICE')
        #Validate if the products (Names) are present in the cart
        cart_product_names = [
            self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[2]').text,
            self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[2]').text
        ]
        self.assertIn(product_1_name, cart_product_names, 'The first product is missing in the cart')
        self.assertIn(product_2_name, cart_product_names, 'The second product is missing in the cart')
        #Validate if the products (Prices) are present in the cart
        cart_product_prices = [
            self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[3]').text,
            self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[3]').text
        ]
        self.assertIn(product_1_price.replace('$', ''), cart_product_prices, 'The price from the first product is incorrect in the cart')
        self.assertIn(product_2_price.replace('$', ''), cart_product_prices, 'The price from the second product is incorrect in the cart')
        #Calculate the expected total
        int_product_1_price = int(product_1_price.replace('$', ''))
        int_product_2_price = int(product_2_price.replace('$', ''))
        int_total = int_product_1_price + int_product_2_price
        total = str(int_total)
        set_variable('TOTAL', total)
        #Validate if the cart total matches the expected one
        search_total = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/h3').text
        self.assertEqual(search_total, total, 'The total displayed in the cart is incorrect')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

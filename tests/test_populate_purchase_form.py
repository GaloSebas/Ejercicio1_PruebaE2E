import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.webdriver import get_webdriver
from pages.demoblaze_page import DemoblazePage
from utils.helpers import generate_fake_data
from utils.helpers import set_variable, get_variable 

class TestPopulatePurchaseForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_webdriver()
        cls.demoblaze = DemoblazePage(cls.driver)
        cls.demoblaze.go_to_cart()

    def test_populate_purchase_form(self):
        #Generate fake data
        name, country, city, credit_card, month, year = generate_fake_data()
        set_variable('CARD', credit_card)
        set_variable('NAME', name)
        set
        #Click on "Place Order"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/button')))
        self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button').click()
        #Populate the purchase form with fake data
        form_data = [name, country, city, credit_card, month, year]
        for index, value in enumerate(form_data, start=1):
            xpath = f'/html/body/div[3]/div/div/div[2]/form/div[{index}]/input'
            self.driver.find_element(By.XPATH, xpath).send_keys(value)
        #Submit the purchase
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')))
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
        #Validate the purchase flow went as expected
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/h2')))
        purchase_confirmation_message = self.driver.find_element(By.XPATH, '/html/body/div[10]/h2').text
        self.assertEqual(purchase_confirmation_message, 'Thank you for your purchase!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
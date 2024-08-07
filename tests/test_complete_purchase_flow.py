import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.webdriver import get_webdriver
from pages.demoblaze_page import DemoblazePage
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils.helpers import set_variable, get_variable, get_today_date 

class TestCompletePurchaseFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = get_webdriver()
        cls.demoblaze = DemoblazePage(cls.driver)
        cls.demoblaze.go_to_cart()

    def test_complete_purchase_flow(self):
        #Get variables needed for testing
        total = get_variable('TOTAL')
        card = get_variable('CARD')
        name = get_variable('NAME')
        date = get_today_date()
        #Extract all the popup data
        search_popup_data = self.driver.find_element(By.XPATH, '/html/body/div[10]/p').text
        #Separate the data for each line
        lines = search_popup_data.split('\n')
        #Save each value into different variables for further comparation
        id_value, amount_value, card_value, name_value, date_value = None, None, None, None, None
        for line in lines:
            if line.startswith('Id:'):
                id_value = line.split(': ')[1]
            elif line.startswith('Amount:'):
                amount_value = line.split(': ')[1].split()[0]
            elif line.startswith('Card Number:'):
                card_value = line.split(': ')[1]
            elif line.startswith('Name:'):
                name_value = line.split(': ')[1]
            elif line.startswith('Date:'):
                date_value = line.split(': ')[1]
        #Validate if the total displayed is the expected one
        self.assertEqual(amount_value, total, 'The total displayed in the popup is incorrect')
        #Validate if the card number displayed is the expected one
        self.assertEqual(int(card_value), card, 'The card number displayed in the popup is incorrect')
        #Validate if the Name displayed is the expected one
        self.assertEqual(name_value, name, 'The name displayed in the popup is incorrect')
        #Validate if the Date displayed is the expected one
        self.assertEqual(date_value, date, 'The date displayed in the popup is incorrect')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

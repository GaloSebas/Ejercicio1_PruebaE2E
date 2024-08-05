from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from faker import Faker
import unittest
import random

class e2e_example_demoblaze(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        ser = Service()
        op = webdriver.ChromeOptions()
        op.add_argument('--disable-notifications')
        cls.driver = webdriver.Chrome(service=ser, options=op)
        driver=cls.driver
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.get("https://www.demoblaze.com/")

    '''
    Frequently Used Functions:
    '''
    def select_product(self):
        driver=self.driver
        random_num = random.randint(1,9)
        driver.find_element(By.XPATH, f'/html/body/div[5]/div/div[2]/div/div[{random_num}]/div/div/h4/a').click()
        return

    def obtain_product_info(self):
        global product_name, product_price
        driver=self.driver
        product_name = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/h2').text
        product_price_and_tax = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/h3').text
        product_price = product_price_and_tax.split()[0]
        return product_name, product_price
    
    def add_product(self):
        driver=self.driver
        driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            self.fail("Alert not found.")
        return

    def validate_products_in_cart(self):
        driver = self.driver
        global products_added, fail_message_products_added
        driver.get("https://www.demoblaze.com/cart.html#")
        WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.XPATH, "//table/tbody/tr")))
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
        count = len(rows)
        if count == 2:
            products_added = True
            fail_message_products_added = ''
        else:
            products_added = False
            fail_message_products_added = 'The products are missing in the cart'
        return products_added, fail_message_products_added
    
    def validate_products_names(self):
        driver=self.driver
        global names_validation, fail_message_names_validation
        cart_product_names = [driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[2]').text,
                              driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[2]').text]
        if product_1_name in cart_product_names:
            if product_2_name in cart_product_names:
                names_validation = True
                fail_message_names_validation =''
            else:
                names_validation = False
                fail_message_names_validation = 'The second product is missing in the cart'
        else:
            names_validation = False
            fail_message_names_validation = 'The first product is missing in the cart'
        return names_validation, fail_message_names_validation

    def validate_products_prices(self):
        driver=self.driver
        global prices_validation, fail_message_prices_validation
        cart_product_prices = [driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[3]').text,
                               driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[2]/td[3]').text]
        if product_1_price.replace('$','') in cart_product_prices:
            if product_2_price.replace('$','') in cart_product_prices:
                prices_validation = True
                fail_message_prices_validation =''
            else:
                prices_validation = False
                fail_message_prices_validation = 'The price from the second product is incorrect in the cart'
        else:
            prices_validation = False
            fail_message_prices_validation = 'The price from the first product is incorrect in the cart'
        return prices_validation, fail_message_prices_validation
    
    def validate_total(self):
        driver=self.driver
        global total_validation,fail_message_total_validation, total
        #Calculation of the expected total
        int_product_1_price = int(product_1_price.replace('$',''))
        int_product_2_price = int(product_2_price.replace('$',''))
        int_total = int_product_1_price + int_product_2_price
        total = str(int_total)
        #Comparing the expected total with the one displayed in the cart
        search_total = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/h3').text
        if search_total == total:
            total_validation = True
            fail_message_total_validation =''
        else:
            total_validation = False
            fail_message_total_validation ='The total displayed in the cart is incorrect'
        return total_validation, fail_message_total_validation
    
    def generate_fake_data(self):
        global name, country, city, credit_card, month, year
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        name = first_name + ' ' + last_name
        country = fake.country()
        city = fake.city()
        credit_card = random.randint(1111111111111111,9999999999999999)
        month = fake.month()
        year = fake.year()
        return name, country, city, credit_card, month, year
    
    def populate_form(self, fake_name, fake_country, fake_city, fake_credit_card, fake_month, fake_year):
        driver=self.driver
        fake_data = [fake_name, fake_country, fake_city, fake_credit_card, fake_month, fake_year]
        base_xpath = '/html/body/div[3]/div/div/div[2]/form/div[{}]/input'
        for index, value in enumerate(fake_data, start=1):
            xpath = base_xpath.format(index)
            driver.find_element(By.XPATH, xpath).send_keys(value)
        return
    
    def validate_purchase(self):
        driver=self.driver
        global test_result, fail_message
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/h2')))
        purchase_confirmation_message = driver.find_element(By.XPATH, '/html/body/div[10]/h2').text
        if purchase_confirmation_message == 'Thank you for your purchase!':
            test_result = True
            fail_message = ''
        else:
            test_result = False
            fail_message = 'The purchase flow failed'
        return test_result,fail_message
    
    def search_confirmation_popup(self):
        driver=self.driver
        global id_value, amount_value, card_value, name_value, date_value
        #Extract all the popup data
        search_popup_data = driver.find_element(By.XPATH, '/html/body/div[10]/p').text
        #Separate the data for each line
        lines = search_popup_data.split('\n')
        #Save each value into different variables for further comparation
        id_value = None
        amount_value = None
        card_value = None
        name_value = None
        date_value = None
        #Crop the inittial data string in each variable
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
        return id_value, amount_value, card_value, name_value, date_value
    
    def get_today_date(self):
        global formatted_date
        #Get todays date
        today = datetime.now()
        adjusted_date = today - relativedelta(months=1)
        day = adjusted_date.day
        month = adjusted_date.month
        year = adjusted_date.year
        #Sets the formatting for the date
        formatted_date = f"{day}/{month}/{year}"
        return formatted_date
    
    '''
    Test 1: Add 2 products to the shopping cart
    Test Description: This test is focused on adding two different products to the cart and validate if the cart displays the expected products.
    '''    
    def test_add_products(self):
        driver=self.driver
        global product_1_name,product_1_price
        global product_2_name,product_2_price
        #Search and add product 1
        self.select_product()
        self.obtain_product_info()
        self.add_product()
        product_1_name, product_1_price= product_name, product_price
        #Go 2 Home again
        driver.get("https://www.demoblaze.com/")
        #Search and add product 2
        self.select_product()
        self.obtain_product_info()
        self.add_product()
        product_2_name, product_2_price= product_name, product_price
        #Validate if products were added or not
        self.validate_products_in_cart()
        test_result_tc1, fail_message_tc1 = products_added, fail_message_products_added
        self.assertTrue(test_result_tc1,fail_message_tc1)
        #Test Ready? YES       

    '''
    Test 2: Review the Cart
    Test Description: This test is focused on validating if the cart have the expected products and displays the expected total.
    '''
    def test_review_cart(self):
        #Validate the product names in the cart
        self.validate_products_names()
        if names_validation:
            #Validate the product prices in the cart
            self.validate_products_prices()
            if prices_validation:
                #Validate the total in the cart
                self.validate_total()
                if total_validation:
                    test_result_tc2 = True
                    fail_message_tc2 =''
                else:
                    test_result_tc2 = False
                    fail_message_tc2 = fail_message_total_validation
            else:
                test_result_tc2 = False
                fail_message_tc2 = fail_message_prices_validation
        else:
            test_result_tc2 = False
            fail_message_tc2 = fail_message_names_validation
        self.assertTrue(test_result_tc2, fail_message_tc2)
        #Test Ready? YES   

    '''
    Test 3: Populate the Purchase Form
    Test Description: This test is focused on completing the purchase form.
    '''
    def test_populate_purchase_form(self):
        driver=self.driver
        #Click the Place Order Button
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[6]/div/div[2]/button')))
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button').click()
        #Generate Fake Data
        self.generate_fake_data()
        #Populate the form with the generated data
        self.populate_form(name, country, city, credit_card, month, year)
        #Submit the purchase
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
        #Validate the purchase flow went as expected
        self.validate_purchase()
        test_result_tc3, fail_message_tc3 =test_result,fail_message
        self.assertTrue(test_result_tc3, fail_message_tc3)
        #Test Ready? YES   

    '''
    Test 4: Complete the Purchase
    Test Description: This test is focused on completing the purchase flow.
    '''
    def test_complete_purchase_flow(self):
        #Extract all the data from the confirmation pop-up
        self.search_confirmation_popup()
        #Valiate if each field displays the expected data
        if amount_value == total:
            if int(card_value) == credit_card:
                if name_value == name:
                    self.get_today_date()
                    if date_value == formatted_date:
                        test_result_tc4 = True
                        fail_message_tc4 = ''
                    else:
                        print('asdasdasdasdad' + date_value,formatted_date)
                        test_result_tc4 = False
                        fail_message_tc4 = 'The date value is incorrect'
                else:
                    test_result_tc4 = False
                    fail_message_tc4 = 'The name value is incorrect'
            else:
                test_result_tc4 = False
                fail_message_tc4 = 'The credit card value is incorrect'
        else:
            test_result_tc4 = False
            fail_message_tc4 = 'The displayed amount is incorrect'
        self.assertTrue(test_result_tc4,fail_message_tc4)
        #Test Ready? YES   

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
if __name__=='__main__':
    unittest.main(verbosity = 2)
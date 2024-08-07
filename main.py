import unittest
from HtmlTestRunner import HTMLTestRunner
from tests.test_add_products import TestAddProducts
from tests.test_review_cart import TestReviewCart
from tests.test_populate_purchase_form import TestPopulatePurchaseForm
from tests.test_complete_purchase_flow import TestCompletePurchaseFlow

class TestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.add_products = TestAddProducts()
        cls.add_products.setUpClass()

    def test_01_add_products(self):
        self.add_products.test_add_products()

    def test_02_review_cart(self):
        #Use the same driver from the previous test
        TestReviewCart.driver = self.add_products.driver  
        review_cart = TestReviewCart()
        #review_cart.setUpClass()
        review_cart.test_review_cart()

    def test_03_populate_purchase_form(self):
        # Use the same driver from the previous test
        TestPopulatePurchaseForm.driver = self.add_products.driver  
        populate_form = TestPopulatePurchaseForm()
        #populate_form.setUpClass()
        populate_form.test_populate_purchase_form()

    def test_04_complete_purchase_flow(self):
        # Use the same driver from the previous test
        TestCompletePurchaseFlow.driver = self.add_products.driver  
        complete_flow = TestCompletePurchaseFlow()
        #populate_form.setUpClass()
        complete_flow.test_complete_purchase_flow()

    @classmethod
    def tearDownClass(cls):
        cls.add_products.tearDownClass()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestSuite))
    runner = HTMLTestRunner(output='reports', report_name='Results_Report', verbosity=2)
    #runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    

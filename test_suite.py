import unittest
import HtmlTestRunner

from e2e_qa_automation_example import e2e_example_demoblaze

# Generate the test suite
def test_suite():
    suite = unittest.TestSuite()
    # Add each TC to define an execution order
    suite.addTest(e2e_example_demoblaze('test_add_products'))
    suite.addTest(e2e_example_demoblaze('test_review_cart'))
    suite.addTest(e2e_example_demoblaze('test_populate_purchase_form'))
    suite.addTest(e2e_example_demoblaze('test_complete_purchase_flow'))
    return suite

if __name__ == '__main__':
    runner = HtmlTestRunner.HTMLTestRunner(output='Reports', report_name='e2e_Results_Report', verbosity=2)
    runner.run(test_suite())
    

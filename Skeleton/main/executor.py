import unittest
import HtmlTestRunner

from Skeleton.main import baseConfigBuilder
from Skeleton.tests.login import LoginTests


def suite():

    suite = unittest.TestSuite()
    suite.addTest(LoginTests('test_InvalidLogin'))
    # suite.addTest(LoginTests('test_ValidLogin'))

    # or there is a way to load tests
    # get all the test from login tests
    # unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    # create a test suite combining LoginTests and home_page_test
    # test_suite = unittest.TestSuite([home_page_test, LoginTests])
    # run the suite using HTMLTestRunner
    # runner.run(test_suite)
    return suite

if __name__ == '__main__':
    # # open the report file
    # outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")
    #
    # # configure HTMLTestRunner options
    # runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

    runner = HtmlTestRunner.HTMLTestRunner('../report/')
    runner.run(suite())
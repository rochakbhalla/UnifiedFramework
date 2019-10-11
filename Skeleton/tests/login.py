
#Idea is to create tests under this file and add the functional content in the main class based on the page object model
import unittest, logging, json
from Skeleton.main.login import LoginMain
from selenium import webdriver

class LoginTests(unittest.TestCase):

    logging.basicConfig(filename='../logs/app.log', filemode='a', format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    @classmethod
    def setUpClass(LoginTests):
        print("Calling setup method")
        global landing_page
        global driver
        driver = webdriver.Chrome("C:\\Users\\rochakb\\Downloads\\chromedriver_win32\\chromedriver.exe")
        landing_page = LoginMain(driver)

    def test_InvalidLogin(self):
        logging.warning("This test is invalid")
        with open("../config/base.json", "r") as read_file:
            data = json.load(read_file)
            logging.info(data['test'])
        landing_page.login()
        print("Testing Invalid Login")

    def test_VerifyErrors(self):
        print("Testing and verifying errors")

    def test_ValidLogin(self):
        print("Testing Valid Login")

    @classmethod
    def tearDownClass(LoginTests):
        logging.error("Calling teardown method")
        driver.quit()


if __name__ == '__main__':
    unittest.main()

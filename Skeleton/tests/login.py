
#Idea is to create tests under this file and add the functional content in the main class based on the page object model
import unittest, logging, json
from configbuilder import ConfigBuilder
from pojoclass import LoginMain, SearchPage


class LoginTests(unittest.TestCase):

    logging.basicConfig(filename='../logs/app.log', filemode='a', format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def setUpClass(self):
        print("Calling setup method")
        
        self.driver = ConfigBuilder.getdriver()
        # driver = webdriver.Chrome("C:\\Users\\rochakb\\Downloads\\chromedriver_win32\\chromedriver.exe")
        #I think here it should call a method from a baseConfigBuilder and which should return the driver 
        
        # driver = baseConfigBuilder.ConfigBuilder("../config/base.json").configure_testbed()
        
        # Create instance variable for all the Object Classes
        self.landing_page = LoginMain(self.driver)
        self.search_page = SearchPage(self.driver)

    def test_InvalidLogin(self):
        logging.info("This test is invalid")
        # val = jsonReader.getvalue(key="tests", filename="base.json")
        # logging.info("The value of the key is the --> "+ val)
        self.landing_page.login()
        print("Testing Invalid Login")
    

    def test_SearchSomething(self):
        print("enter the id and test somethng")
        self.search_page.search_string("gLFyf gsfi")

    def test_ValidLogin(self):
        print("Testing Valid Login")

    def tearDownClass(self):
        logging.error("Calling teardown method")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


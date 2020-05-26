import logging

class LoginMain:
    logging.basicConfig(level=logging.INFO, filename='../logs/app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://google.com")
        logging.info("Rochak Bhalla has run one test")

        print(self.driver)

class SearchPage:

    def __init__(self, driver):
        self.driver = driver
    
    def search_string(self, value):
        self.driver.find_element_by_class(value)


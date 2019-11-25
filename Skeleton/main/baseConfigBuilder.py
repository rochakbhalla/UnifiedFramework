# To build the execution cycle based upon the base configuration

import json
import logging
from selenium import webdriver


class ConfigBuilder:

    def __init__(self, file_path_config):
        self.filePathConfig = file_path_config
        self.config_data = self.read_json(self.filePathConfig)

    @staticmethod
    def read_json(file_path_config):
        with open(file_path_config, 'r') as keys:
            base_data = json.load(keys)
            if type(base_data) is not dict:
                logging.error("Base data is not of Dict type.")
        return base_data

    def get_env(self):
        env = self.config_data.get("environment")
        if env.upper() in ["QA", "STAGING", "PRODUCTION", "PROD"]:
            return env
        else:
            msg = "Environment not supported"
            raise BaseException(msg)

    def configure_testbed(self):
        tb = self.config_data.get("test_bed")
        for i in tb:
            if i.casefold() == 'UI'.casefold():
                chromedriver = webdriver.Chrome("C:\\Users\\rochakb\\Downloads\\chromedriver_win32\\chromedriver.exe")
                firefoxdriver = webdriver.Firefox("C:\\Users\\rochakb\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe")
                return chromedriver, firefoxdriver
            elif i.casefold() == 'API'.casefold():
                pass
            elif i.casefold() == 'Database'.casefold():
                pass
            elif i.casefold() == 'Smartphone'.casefold():
                pass
            print(i)

#
# cb = ConfigBuilder("../config/base.json")
# # print(cb.get_env())
# print(cb.configure_testbed())
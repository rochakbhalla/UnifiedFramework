#To build the execution cycle based upon the base configuration

import json
class ConfigBuilder():


    def __init__(self, filePathConfig):
        with open(filePathConfig, 'r') as keys:
            config_data = json.load(keys)
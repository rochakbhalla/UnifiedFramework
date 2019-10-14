import json, logging



def getKey(self, value, filename):
    pass


def getvalue(key, filename):
    logging.debug(filename + ", -->"+"../config/"+filename)
    with open("../config/"+filename, "r") as read_file:
        data = json.load(read_file)
        while type(data[key]) is dict:
            key = dict(data[key]).get("test1")
            data[key] = key
        else:
            return data[key]



if __name__ == '__main__':
    val = getvalue(key='tests', filename='base.json')
    print(val)
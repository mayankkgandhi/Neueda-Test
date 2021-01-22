from json import dumps, loads
from os import listdir

def get_json_files():
    """
    Function to get json files
    :return: json files from directory  
    """
    return lambda filename: filename[-5:] == '.json', listdir("jsons/")


def read_json(file):
    """
    Function to read json data
    :param: file - json file to read
    :return: data - data from json file
    """
    with open("/jsons/" + file, "r") as json_file:
        data = json_file.read()
    try:
        data = dumps(loads(data))
    except ValueError as ve:
        print("Unable to parse file, json expected!")

    return data
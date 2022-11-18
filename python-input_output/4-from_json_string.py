#!/usr/bin/python3
# from json to python object
# json sting to object
''' by defining a function '''
import json


def from_json_string(my_str):
    ''' defining a function that convert json string to 
    python object '''
    return json.loads(my_str)

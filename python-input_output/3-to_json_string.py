#!/usr/bin/python3
# to json object
# we are going to return json string
''' defining function that do it '''
import json


def to_json_string(my_obj):
    ''' a function that convert dict to json object '''
    return json.dumps(my_obj)

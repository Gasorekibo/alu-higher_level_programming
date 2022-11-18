#!/usr/bin/python3
# save object to a file
# json usage to save object to file
''' we'are going to define a function '''
import json


def save_to_json_file(my_obj, filename):
    ''' defining a function that save object to a file '''
    with open(filename, 'w', encoding='utf-8')as f:
        return json.dump(my_obj, f)

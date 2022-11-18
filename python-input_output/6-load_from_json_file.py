#!/usr/bin/python3
# Create object from a JSON file
# create an object form json file
''' we are going to import json module '''
import json


def load_from_json_file(filename):
    ''' defining a function to perform task '''
    with open(filename, 'r', encoding='utf-8')as f:
        return json.load(f)

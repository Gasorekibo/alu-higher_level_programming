#!/usr/bin/python3
"""
    a base class that inherit from object
"""
import json


class Base:
    """
        a class with private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            a instance method with one instace attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ json string representation of list_dictionary """
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

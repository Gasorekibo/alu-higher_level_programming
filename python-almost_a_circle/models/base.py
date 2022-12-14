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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json string representation of list_dictionary """
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ json string representation to file object """
        filename = cls.__name__ + ".json"
        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))
            with open(filename, 'w') as file:
                file.write(cls.to_json_string(new))

#!/usr/bin/python3
"""
    a base class that inherit from object
"""
import json
import os.path
import csv


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
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write('[]')
            else:
                file.write(cls.to_json_string([i.to_dictionary()
                                              for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ return list of json string """
        if json_string is None:
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returning all instances and attributes set before """
        if cls.__name__ == "Rectangle":
            inst = cls(10, 10)
        else:
            inst = cls(10)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """ a function that return a list of instance """
        filename = "cls.__name__.json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as new:
            list_inst = new.read()
        list_cls = cls.from_json_string(list_inst)
        result = []
        for i in range(len(list_cls)):
            result.append(cls.create(**list_cls[i]))
        return result

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ updating """
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']
        matrix = []
        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])
            with open(filename, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(matrix)

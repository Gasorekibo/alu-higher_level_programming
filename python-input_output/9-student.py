#!/usr/bin/python3
# Student to JSON
#  a class Student that defines a student
''' defining a class with puplic instance '''


class Student:
    ''' defining a class with public instance '''
    def __init__(self, first_name, last_name, age):
        ''' instation of the class method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        ''' convert to json '''
        return json.load(__dict__)

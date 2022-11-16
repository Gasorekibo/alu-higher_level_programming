#!/usr/bin/python3
# improve Geometry
# based on 5_base_python.py
''' raise and exception '''


class BaseGeometry:
    ''' class that raise an exception '''
    def area(self):
        ''' a function that raise an exception '''
        raise Exception("area() is not implemented")

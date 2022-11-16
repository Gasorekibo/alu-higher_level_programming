#!/usr/bin/python3
# improve Geometry
# based on 7_base_python.py
''' raise and exception '''


class BaseGeometry:
    ''' class that raise an exception '''
    def area(self):
        ''' a function that raise an exception '''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        ''' check if value is integer or not '''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
class Rectangle(BaseGeometry):
    ''' inherting BaseGeometry '''
    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

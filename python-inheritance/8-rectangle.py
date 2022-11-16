#!/usr/bin/python3
# improve Geometry
# based on 7_base_python.py
''' raise and exception '''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' inherting BaseGeometry '''
    
    def __init__(self, width, height):
        
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

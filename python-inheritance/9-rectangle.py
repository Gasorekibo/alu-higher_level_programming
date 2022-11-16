#!/usr/bin/python3
# Full rectangle
# based on 8-rectangle.py
''' we allowed to import module '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' defining Rectangle class that inherit from
    BaseGeometry '''
    def __init__(self, width, height):
        ''' instatiation '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height' = height)
        self.__height = height
    def area(self):
        ''' returning the area of Rectangle '''
        return(self.__width * self.height)
    def __str__(self):
        ''' printing the area using __str__ method '''
        return f'[Rectangle] {self.width} / {self.height}'

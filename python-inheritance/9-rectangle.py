#!/usr/bin/python3
# class 'Rectangle' that inherits from 'BaseGeometry' (7-base_geometry.py)
# (task based on 8-rectangle.py)
"""
    define a class 'Rectangle' inheriting from 'BaseGeometry'
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
       class Rectangle
    """
    def __init__(self, width, height):
        """
           initialize new 'rectangle'
           args:
           width(int): width of the new rectangle
           height (int): height of the new rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return the are of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ print string """
        return f"[Rectangle] {self.__width}/{self.__height}"

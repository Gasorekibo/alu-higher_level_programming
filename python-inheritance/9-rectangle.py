#!/usr/bin/python3
# class 'Rectangle' that inherits from 'BaseGeometry' (7-base_geometry.py)
# (task based on 8-rectangle.py)
"""
    define a class 'Rectangle' inheriting from 'BaseGeometry'
    """
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    '''defining Rectaangle class '''
    def __init__(self, width, height):
        """instationing class method"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
    def area(self):
        ''' return area of rectangle '''
        return(self.__width * self__height)
    def __str__(self):
        """ print string """
        return f'[Rectangle] {self.__width}/{self.__height}'

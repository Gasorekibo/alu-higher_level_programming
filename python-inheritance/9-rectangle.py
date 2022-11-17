#!/usr/bin/python3
# define Rectangle class
# inherited from 8_BaseGeometry
''' we allowed to import module '''
Rectangle = __import__('7-base_geometry.py').Rectangle


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

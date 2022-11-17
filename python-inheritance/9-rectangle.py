#!/usr/bin/python3
# Full rectangle
# rectangle that inherit from BaseGeometry
''' allowe to import module '''
BaseGeometry = __import__(7-base_geometry.py).BaseGeometry

class Rectangle(BaseGeometry):
    ''' instantioning Rectangle class '''
    def __init__(self, width, height):
        ''' the method has two
            args:
              width and height
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
    def area(self):
        ''' return the area of rectangle '''
        return self.__width * self.__height
    def __str__(self):
        ''' printing is string format '''
        return f'[Rectangle] {self.__width} / {self.__width}'

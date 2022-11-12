#!/usr/bin/python3
# Simple rectangle
''' creating an empty rectangle class '''


class Rectangle:
    ''' a class rectangle that define rectangle '''
    def __init__(self, width=0, height=0):
        ''' initializing the class instances
            args:
            it has 2 args width and height '''
            self.width = width
            self.height = height
    
    @property
    def width(self):
        '''defining private attribute '''
        return self.__width
    
    @width.setter
    def width(self, value):
        ''' checking if the private attribute meet the condition to be retrieve '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        ''' retrieving the actual private atribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' checking wether private attribute met the condition to be changed '''
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

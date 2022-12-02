#!/usr/bin/python3
# Simple rectangle
# based on the 0-rectangle.py
''' creating an empty rectangle class '''


class Rectangle:
    ''' a class rectangle that define rectangle '''
    def __init__(self, width=0, height=0):
        ''' initializing the class instances
            args:
                width(int): it is a width of rectangle
                rectangle(int): it is a height of rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''defining private attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' checking if the private attribute meet
        the condition to be retrieve
            args:
                it has only one argument value'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' retrieving the actual private atribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' checking wether private attribute met
        the condition to be changed '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' returning the area of rectangle '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' returning the perimeter of rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ returnin the rectangle with # pattern """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        else:
            for i in range(self.__height):
                string += "#" * self.__width
                if i < self.__height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """ return the rectangle as string """
        return Rectangle("{}, {}".format(self.__width, self.__height))

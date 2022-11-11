#!/usr/bin/python3
# a class that define an area of a square
'''defining a class'''


class Square:
    ''' instationing the private attribute'''
    def __init__(self, size=0):
        self.__size = size
        '''checking the condition of attribute'''
        if size not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        '''return the area of square'''
        return self.__size * self.__size

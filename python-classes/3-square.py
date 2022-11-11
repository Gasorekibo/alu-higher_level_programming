#!/usr/bin/python3
# 3-square.py

# defining how this module is going to work in the following class

"""Area square: """


class Square:
    ''' instationing the private attribute'''
    
    def __init__(self, size=0):
        ''' Args:

                size (int): size of the new square
        '''
        if size not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        '''return the area of square'''
        return self.__size * self.__size

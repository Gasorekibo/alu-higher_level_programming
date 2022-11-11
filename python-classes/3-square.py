#!/usr/bin/python3
# a class that define an area of a square
'''
definng a class

'''


class Square:
    ''' instationing the private attribute'''
    def __init__(self, size=0):
        self.__size = size
        '''checking the condition of attribute'''
        if size not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    '''declaring a method that calculate the area of square'''
    def area(self):
        Area = self.__size ** 2
        return Area

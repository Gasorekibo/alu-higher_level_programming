#!/usr/bin/python3
# A class that define square with private attribute
''' Size private attribute shoud be an interger'''


class Square:
    '''instantition the class private attribute'''
    def __init__(self, size=0):
        '''checking the condition'''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

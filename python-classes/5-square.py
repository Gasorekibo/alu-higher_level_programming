#!/usr/bin/python3
# a class Square that defines a square by: (based on 4-square.py)
# but at this time we will add a private instance attribute
'''
   define a class 'Square'
'''


class Square:
    '''
       this class will contain __init__ module, and attributes
    '''
    def __init__(self, size=0):
        ''' this is an __init__ method, it has characters of an object '''
        self.size = size

    @property
    def size(self):
        ''' this is a private instance attribute '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' stting the value of a size '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        ''' this function will return the area of the current square '''
        return (self.__size * self.__size)

    def my_print(self):
        ''' prints square with character # '''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

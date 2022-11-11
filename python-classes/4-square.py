#!/usr/bin/python3
# a class Square that defines a square
# documenting the how the module will work in the following class
'''by refering to question 3'''


class Square:
    '''
    instatioting private attribute'''
    
    def __init__(self, size=0):
        '''args:
                size (int): size of the new square'''
        
        self.__size = size
    
    @property
    def size(self):
        '''detter application'''

        return self.__size
    
    @size.setter
    def size(self.value):
        '''check if size is interger and if is greater that zero'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        '''returning the area of square'''
        return self.size * self.size


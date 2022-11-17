#!/usr/bin/python3
# Square class
# that inherit from Rectangle in question 9
''' we are allowed to import module '''
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    ''''instationing Square class '''
    def __init__(self, size):
        ''' function has one arguments
            size(int): the size of new square
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


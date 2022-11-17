#!/usr/bin/python3
# class 'Square' that inherits from 'Rectangle'
# (9-rectangle.py)
"""
   define a class 'Square' inheriting from 'BaseGeometry'
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ defining class 'Square'"""
    def __init__(self, size):
        """ instantiation a new square
           args:
               size(int): the size of the class 'square'
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

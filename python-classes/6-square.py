#!/usr/bin/python3
# defining the way module will work in the following class
# defining the coordinate of square
# They are different types of instance that we are going to deal with in the following project
"""
   a class Square that defines a square by
   based on 5.square.py
"""


class Square:
    """
       square with private instance attribute: 'size'
    """
    def __init__(self, size=0, position=(0, 0)):
        """
           args:
               size (int): size of the new square
        """
        self.size = size
        self.position = position
    @property
    def size(self):
        """
           gets current size of the square
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
           validates size is an integer that is greater than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        """
           gets the current position of the square
        """
        return self.__position
    @position.setter
    def position(self, value):
        """
           set position
           args:
               value: position of the square
        """
        if not(isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        """
           Return: area of the square
        """
        return self.__size * self.__size
    def my_print(self):
        """
           prints square with character #
        """
        if size == 0:
            print("")
            return 
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

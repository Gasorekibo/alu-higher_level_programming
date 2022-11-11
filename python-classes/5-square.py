#!/usr/bin/python3
# Printing a square
""" defining square class """


class Square:
    """square class created"""
    
    def __init__(self, size=0):
        """instationing the attribute"""
        self.size = size
    @property
    def size(self):
        """detter method to retrive the private attribute"""
        return sef.__size
    @size.setter
    def size(self, value):
        """updating private attribute if it is interger and greater that zero"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """returning the are of square"""
        return(self.__size * self.__size)
    def def my_print(self):
        """printing the square with the # if size != 0"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

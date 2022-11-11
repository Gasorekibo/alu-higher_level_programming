#!/usr/bin/python3
# class 'Square' that defines a square by:
# (based on 5-square.py)
"""
   define a class 'Square'
"""


class Square:
    """
       class with private attribute
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
        return self.size
    
    @size.setter
    def size(self, value):
        """
          validates size is an integer that is greater than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """
          Return: area of the square
        """
        return(self.__size * self.__size)
    
    def my_print(self):
        """
          prints square with character #
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
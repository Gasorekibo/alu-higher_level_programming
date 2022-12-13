#!usr/bin/python3
"""
   square class that inherit from rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        a square class inherit from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            class constructor with four given attribute
        """
        super().__init__(size, size, x=0, y=0, id=None)
    @property
    def width(self):
        """ getter for width """
        return self.__width
    @width.setter
    def width(self, size):
        """ setter for width """
        self.__width = size

    @property
    def height(self):
        """ getter for height """
        return self.__height
    @height.setter
    def height(self, size):
        """ setter for height """
        self.__height = size

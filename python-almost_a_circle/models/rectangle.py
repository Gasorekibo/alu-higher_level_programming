#!/usr/bin/python3
"""
    a rectangle class inherit from base class
"""
from models.base import Base


class Rectangle(Base):
    """
        inheriting form Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            instantion of rectangle class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter of with """
        return self.__width

    @width.setter
    def width(self, width):
        """ checking if value meet the condition """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter for height instance """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter for hight """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def y(self):
        """ getter of y instance """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter of y instance """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def x(self):
        """ getter of x instance """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter of x instance """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

    def area(self):
        """ returning the are of rectangle """
        return(self.width * self.height)

    def display(self):
        """ printing a rectangle with # character """
        for i in range(self.width + 1):
            for j in range(self.height + 1):
                print("#", end='')
            print()

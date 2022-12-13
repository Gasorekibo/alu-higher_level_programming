#!/usr/bin/python3
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
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """ getter for width """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for width """
        self.width = value
        self.height = value

    def __str__(self):
        """ print a in str format """
        return("[Square] {} {}/{} - {}".format(self.id, self.x, self.y,
                                               self.width))

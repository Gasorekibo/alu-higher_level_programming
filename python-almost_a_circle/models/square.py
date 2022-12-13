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
        super().__init__(size, size, x=0, y=0, id=None)
    
    @property
    def size(self):
        """ getter for width """
        return self.width
    
    @size.setter
    def size(self, value):
        """ setter for width """
        self.width = value
        self.height = value

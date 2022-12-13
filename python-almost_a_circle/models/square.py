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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ assign variable to attribute """
        if len(args) != 0 and args is not None:
            attributes = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attributes[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'heidth', value)
                else:
                    setattr(self, key, value)


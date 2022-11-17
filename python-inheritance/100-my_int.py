#!/usr/bin/python3
# class Myint
# inhertit from int
""" this is advanced task """


class Myint(int):
    """ 
      invert int operators '==' and '!='
    """
    
    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value

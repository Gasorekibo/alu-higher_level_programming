#!/usr/bin/python3
# a function that add two integer
"""
    both a and b must be an interger and we will return a+b
"""


def add_integer(a, b=98):
    """ 
        argument: a and b of type int
        return the a+b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return(int(a) + int( b))

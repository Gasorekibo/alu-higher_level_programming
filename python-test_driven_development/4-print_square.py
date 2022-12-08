#/usr/bin/python3
# a function that print square wiht # character
"""
    a function will have size argument of type int
"""
def print_square(size):
    """
        argument: size fo type int
        will return a square with # character
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")

#!/usr/bin/python3
def no_c(my_string):
    if ord('c'):
        return my_string.translate({ord('c'): None})
    elif ord("C"):
        return my_string.translate({ord('C'): None})
    else:
        return my_string

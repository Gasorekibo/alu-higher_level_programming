#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(i))
            return True
        else:
            return False
    except Exception as ex:
        return(ex)

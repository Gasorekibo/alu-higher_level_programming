#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in value:
            if isinstance(i, int):
                print("{:d}".format(i))
                return True
            else:
                return False
    except Exception as ex:
        return(ex)

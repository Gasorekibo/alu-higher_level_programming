#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        pass
    finally:
        if b != 0:
            print("Inside result: {}".format(result))
            return result
        else:
            print("Inside result: {}".format(None))
            return None

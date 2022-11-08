#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except Exception as ex:
        pass
    finally:
        if b != 0:
            print("Inside result:{}".format.(result))
        else:
            return None

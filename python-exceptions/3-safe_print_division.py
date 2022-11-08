#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except Exception as ex:
        print(ex)
    finally:
        if b != 0:
            print("{}".format.(result))
        else:
            return None

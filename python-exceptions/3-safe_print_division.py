#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b != 0:
            result = a / b
            print("Inside result: {}".format(result))
    except Exception as ex:
        pass
    finally:
        if b == 0:
            result = None
            print("{} / {} = {}".format(a, b, result))

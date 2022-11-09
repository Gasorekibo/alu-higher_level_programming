#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        def division(a, b):
            print("Inside result: {}".format(result))
    except Exception as ex:
        pass
    finally:
        if b != 0:
            print(result)
        else:
            return None

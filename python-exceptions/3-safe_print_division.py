#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        def division(a,b):
            result = a/b
            return("Inside result: {}".format(result))
        except Exception as ex:
        pass
    finally:
        if b != 0:
        division(a,b)
        else:
            return None

#!/usr/bin/python3
def safe_print_integer(value):
    try:
        for i in value:
            if isinstance(value[i], int):
                return True
            else:
                return False
    except Exception as ex:
        print(ex)

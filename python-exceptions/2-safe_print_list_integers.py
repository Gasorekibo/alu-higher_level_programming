#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if isinstance(x,int) and x <= range(my_list):
            print("{:d}".format(x)
        else:
            continue
    except Exception as ex:
        print(ex)

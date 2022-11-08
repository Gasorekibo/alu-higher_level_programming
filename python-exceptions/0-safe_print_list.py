#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = []
        for i in range(x):
            new_list+= i
        print("{}".format(new_list), end= "")
    except Exception as ex:
        return ex


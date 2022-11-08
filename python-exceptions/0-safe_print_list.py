#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    num = 0
    for i in my_list:
        lenght+= 1
    for j in range(x):
        try:
            print("{}".format(my_list(j)), end= "")
            print("")
        except:
            return length
        num += 1
    print("")
    return num

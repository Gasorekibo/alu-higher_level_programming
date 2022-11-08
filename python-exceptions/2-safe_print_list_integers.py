#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    num = 0
    for i in my_list:
        length += 1
    for j in range(x):
        try:
            if isinstance(j, int) and j <= range(x):
                print("{:d}".format(m_list[j]), end="")
            else:
                pass
        except:
            print("")
            return length
        num += 1
    print("")
    return num

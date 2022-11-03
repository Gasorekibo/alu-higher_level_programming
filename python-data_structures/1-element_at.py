#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return none
    elif idx > len(my_list)-1:
        return none
    else:
        print("Element at index {} is {}".format(idx, my_list[idx]))

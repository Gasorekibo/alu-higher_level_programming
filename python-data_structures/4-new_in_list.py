#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        x = my_list.copy()
        return x
    else:
        for i in my_list:
            new_list = []
            if i == idx:
                new_list.insert(idx,element)
                return new_list
            else:
                return my_list

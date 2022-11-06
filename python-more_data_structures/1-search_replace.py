#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
         new_list = my_list.copy()
         if new_list == search:
             new_list.append(replace)
    return new_list

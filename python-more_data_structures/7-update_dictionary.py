#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if i in a_dictionary:
            a_dictionary[key] = value
        elif i not in a_dictionary:
            a_dictionary[key] = value
        return a_dictionary


#!/usr/bin/python3
def best_score(a_dictionary):
    for value, key in a_dictionary.items():
        if value in a_dictionary:
        a_dictionary[key] = max(value)
    return a_dictionary
    else:
        return None


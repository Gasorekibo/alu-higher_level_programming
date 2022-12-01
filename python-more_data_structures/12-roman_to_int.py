#!/usr/bin/python3
from functools import reduce
def roman_to_int(roman_string):
    list1 = []
    list2 = []
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 100}
    if roman_string not in dictionary.keys():
        return 0
    else:
        for i in roman_string:
            for j in dictionary:
                if i == n:
                    list1.append(dictionary[j])
                    a = reduce(map(lambda x, y : y - x if y > x else x + y), list1)
        list2.append(a)
        return list2

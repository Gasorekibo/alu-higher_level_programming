#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    sorted_people = sorted(a_dictionary.items(), key=lambda item: item[1])
    sorted_people_dict = {}
    for key, value in sorted_people:
        sorted_people_dict[key] = value*2
    print(sorted_people_dict)

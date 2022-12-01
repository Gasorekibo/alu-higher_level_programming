#!/usr/bin/python3
def weight_average(my_list=[]):
    a = len(my_list)
    b = 0
    value = 0
    result = 0
    if my_list = []:
        return 0
    else:
        while b < a:
            m = my_list[b][0] * my_list[b][1]
            value += m
            i = my_list[b][1]
            result += i
            b += 1
        return value/result

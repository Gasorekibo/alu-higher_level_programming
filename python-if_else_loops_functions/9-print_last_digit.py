#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        y = ((number * -1) % 10) * -1
        print(y)
    else:
        x = (number%10)
        print(x)

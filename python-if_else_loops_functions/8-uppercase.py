#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            l = ord(i) - 32
        else:
            l = ord(i) - 32
        print("{:s}".format(chr(l)), end=" ")

#!/usr/bin/python3
for i in range(0, 9):
    for d in range(i+1, 10):
        if i == 8:
            print("{}{}".format(i, d))
        else:
            print("{}{}".format(i, d), end=", ")

#!/usr/bin/python3
# Read file
# input and output file
''' a function that read a file '''


def read_file(filename=""):
    ''' reading the file using with '''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(),end="")

#!/usr/bin/python3
# append to a file
# a function that append to a file and return
''' number of characters added '''


def append_write(filename="", text=""):
    ''' a function that append to a file '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

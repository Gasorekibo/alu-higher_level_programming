#!/usr/bin/python3
# write to a file
# writing string to a file
''' starting by writing a fucntion '''


def write_file(filename="", text=""):
    ''' a function that write a text to a fie '''
    with open(filename, 'w', encoding='utf-8')as f:
        return f.write(text)

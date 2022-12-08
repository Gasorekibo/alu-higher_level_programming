#!/usr/bin/python3
# a function that print text with two lines after
"""
    each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        argument: text of type string
        return a text with 2 space after special character
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        value = 0
        while value < len(text) and text[value] == ' ':
            value += 1
        while value < len(text):
            print(text[value], end="")
            if text[value] == "\n" or text[value] in ".?:":
                if text[value] in ".?:":
                    print("\n")
                value += 1
                while value < len(text) and text[value] == ' ':
                    value += 1
                continue
            value += 1

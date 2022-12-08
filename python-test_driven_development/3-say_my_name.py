#!/usr/bin/python3
# a function a that say first and second name
"""
    first name and second name must be string type
"""


def say_my_name(first_name, last_name=""):
    """
        arguments:
            first name: is string type
            second name: is string type
        it will return name as My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

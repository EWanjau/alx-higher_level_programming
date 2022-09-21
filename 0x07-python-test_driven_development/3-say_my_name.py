#!/usr/bin/python3
""" this module has function that prints
a name
"""


def say_my_name(first_name, last_name=""):
    """prints name
    args:
        first_name: name
        last_name: name
    result: string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

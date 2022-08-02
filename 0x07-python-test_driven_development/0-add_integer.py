#!/usr/bin/python3
""" this module adds two numbers
and tests the inputs
"""


def add_integer(a, b=98):
    """function for the addition of the two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)

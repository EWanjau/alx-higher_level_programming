#!/usr/bin/python3
""" this module has function that prints
a square using hash symbol
"""


def print_square(size):
    """prints square
    args:
        size: the dimensions of the square
    result: square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)

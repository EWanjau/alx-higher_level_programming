#!/usr/bin/python3
"""addition module
"""


def add_integer(a, b=98):
    """this function adds two integers
            args:
                a = 1st parameter
                b = 2nd parameter
            output:
                addition
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
        return a + b
    else:
        return a + b

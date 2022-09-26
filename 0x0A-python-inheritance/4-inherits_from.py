#!/usr/bin/python3
"""Module 4-inherits_from.
check status
"""


def inherits_from(obj, a_class):
    """returns true for inherited atrributes

    Args:
        - obj: object to look
        - a_class: class to compare
    Returns: True if object is an instance of a_class
    """

    return isinstance(obj, a_class) and type(obj) != a_class

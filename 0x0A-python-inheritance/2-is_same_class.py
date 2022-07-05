#!/usr/bin/python3
"""Module 2-is_same_class
check status
"""


def is_same_class(obj, a_class):
    """returns true for same instance

    Args:
        - obj: object to look
        - a_class: class to compare
    Returns: True if object is an instance of a_class
    """

    return True if type(obj) is a_class else False

#!/usr/bin/python3
"""Module 3-is_kind_of_class
check status
"""


def is_kind_of_class(obj, a_class):
    """returns true for same instance

    Args:
        - obj: object to look
        - a_class: class to compare
    Returns: True if object is an instance of a_class
    """

    return isinstance(obj, a_class)

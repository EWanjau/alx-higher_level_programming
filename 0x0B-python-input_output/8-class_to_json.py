#!/usr/bin/python3
"""Module 8-class_to_json
returns a dictionary
"""


def class_to_json(obj):
    """creates json object from python class

    Args:
        - object: python object
    Return: JSON serialization of an object

    """
    return obj.__dict__

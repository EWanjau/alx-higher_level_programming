#!/usr/bin/python3
"""Module 4-from_json_string
returns a python object from JSON representation of an object.
"""


def from_json_string(my_str):
    """gets python object from JSON representation

    Args:
        - my_obj: object to transform
    Return: python object equivalent
    """
    import json
    return json.loads(my_str)

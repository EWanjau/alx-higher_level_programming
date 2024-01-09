#!/usr/bin/python3
"""Module 3-to_json_string
returns a JSON representation of an object.
"""


def to_json_string(my_obj):
    """gets JSON representation

    Args:
        - my_obj: object to transform
    Return: JSON equivalent
    """
    import json
    return json.dumps(my_obj)

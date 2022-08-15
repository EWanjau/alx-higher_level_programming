#!/usr/bin/python3
"""class that defines a Base"""


import json


class Base:
    """the attributes and methods
    defining the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """display json rep of all dictionaries"""
        if list_dictionaries is None and list_dictionaries == []:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

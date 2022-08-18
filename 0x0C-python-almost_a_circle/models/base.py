#!/usr/bin/python3
"""class that defines a Base"""


import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """display json rep of all dictionaries"""
        if list_dictionaries is None and list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json rep to a file"""
        if list_objs is None:
            name = "[]"
        else:
            name = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(name)

    @staticmethod
    def from_json_string(json_string):
        """convert from json to another format"""
        last = []
        if json_string is None or json_string == "[]":
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        last = json.loads(json_string)

        return last

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set"""
        if cls.__name == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if not cls:
            return []
        filename = cls.__name + ".json"
        last = []
        list_dict = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                s = f.read()
                list_dict - cls.from_json_string(s)
                for d in list_dict:
                    last.append(cls.create(**d))
        return last

#!/usr/bin/python3
"""class student
describes a student
"""


class Student():
    """Describes a student"""
    def __init__(self, first_name, last_name, age):
        """initialize instances of students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of students"""
        if attrs is not None:
            stud_dict = {}
            for i in self.__dict__:
                if i in attrs:
                    stud_dict[i] = self.__dict__[i]
            return stud_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all the attributes of the Student instance"""
        if json:
            self.__dict__ = json

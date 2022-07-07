#!/usr/bin/python3
"""Class 9-student
describes a student
"""


class Student():
    """Describes a student"""
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """initialize instances of students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of students"""
        return self.__dict__

#!/usr/bin/python3
"""class student
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

    def to_json(self, attrs=None):
        """retrieves dictionary representation of students"""
        if attrs is not None:
            stud_dict = {}
            for i in vars(self):
                if i in attrs:
                    stud_dict[i] = vars(self)[i]
            return stud_dict
        else:
            return vars(self)

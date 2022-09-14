#!/usr/bin/python3
""" module defines a class square
"""


from curses import setupterm
from sys import settrace


class Square():
    """defines an empty class and raises exception"""
    def __init__(self, size=0):
        """initializes the objects"""
        self.size = size

    def area(self):
        """calculates the area of the square instances"""
        return self.__size * self.__size

    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of instance attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

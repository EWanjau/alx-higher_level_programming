#!/usr/bin/python3
"""Square Class"""


class Square():
    """ class square defines a square"""
    def __init__(self, size=0):
        """the valid size square before initialization"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """finds the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """retrieves info from a private attribute of an object"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value to retrieve"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints a square of size specified by argument"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):
                print("#" * self.__size)

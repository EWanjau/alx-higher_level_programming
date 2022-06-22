#!/usr/bin/python3
"""Square Class"""


class Square():
    """ class square defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialization square attributes"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves info from a private attribute of an object"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of the position attribute
            Args:
                value: to be set
            Return: the set value
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints a square of size specified by argument using #"""
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

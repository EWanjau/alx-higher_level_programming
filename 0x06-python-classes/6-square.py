#!/usr/bin/python3
""" module defines a class square
"""


class Square():
    """defines an empty class and raises exception"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the objects"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets the property"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of the position"""
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
        """prints the square on stdout using #"""
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

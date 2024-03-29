#!/usr/bin/python3
"""class for rectangle"""


class Rectangle():
    """the class defines width and height of rectangle"""
    def __init__(self, width=0, height=0):
        """the initialization of an instance of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width is a private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width to the value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height attribute"""
        return self.__height

    @height.setterd
    def height(self, value):
        """set the value of the height ot a specified value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    
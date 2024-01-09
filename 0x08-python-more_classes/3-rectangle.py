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

    @height.setter
    def height(self, value):
        """set the value of the height ot a specified value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        _area = self.__height * self.__width
        return _area

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            _perimeter = 0
        else:
            _perimeter = 2 * (self.__height + self.__width)
        return _perimeter

    def print(self):
        """print the rectangle with a character"""
        for col in range(self.__width):
            for row in range(self.__height):
                print("#")

    def __str__(self):
        """print the rectangle with a '#' character"""
        if self.__width == 0 or self.__height == 0:
            return ""

        str_space = ''
        for col in range(self.__height):
            for row in range(self.__width):
                str_space += "#"
            str_space += '\n'
        return str_space[:-1]

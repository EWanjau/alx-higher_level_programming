#!/usr/bin/python3
"""Module 8-rectangle
raises error exception and validates value
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from base geometry"""

    def __init__(self, width, height):
        """validates height
        Args:
            - width: height
            - height: height
        Returns: None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return a string"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """gets the area of rectangle

        Args:
            - width: dimension
            - height: dimension
        return area
        """
        return self.__width * self.__height

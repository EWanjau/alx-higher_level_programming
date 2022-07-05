#!/usr/bin/python3
"""Module 8-rectangle
raises error exception and validates value
"""


class BaseGeometry():
    """raises an error

    Args:
        - None
    Returns: None
    """
    def area(self):
        """raise error exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises an error
        Args:
            - name: name
            - value: value
        Returns: validation
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value


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

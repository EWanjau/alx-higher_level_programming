#!/usr/bin/python3
"""Module 8-rectangle
raises error exception and validates value
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from base geometry"""

    def __init__(self, size):
        """validates height
        Args:
            - width: height
            - height: height
        Returns: None
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """gets the area of rectangle

        Args:
            - None
        return area
        """
        return self.__size ** 2

    def __str__(self):
        """displays the area"""
        return str("[Square] {}/{}".format(self.__size, self.__size))

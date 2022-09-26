#!/usr/bin/python3
"""Module 7-base_geometry
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

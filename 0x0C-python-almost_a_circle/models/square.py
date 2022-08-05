#!/usr/bin/python3
"""class that defines square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return print("[Square] ({}) {}/{} - {}".
                     format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """retrieve value for the attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the value to the attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

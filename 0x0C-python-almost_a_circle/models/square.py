#!/usr/bin/python3
"""class that defines square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.width = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return print("[Square] ({}) {}/{} - {}".
                     format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """retrieve value for the attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value to the attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of the class"""
        new_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return new_dict

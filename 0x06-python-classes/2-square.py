#!/usr/bin/python3
"""Square Class"""


class Square():
    """ class square defines a square"""
    def __init__(self, size=0):
        """the valid size square before initialization"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

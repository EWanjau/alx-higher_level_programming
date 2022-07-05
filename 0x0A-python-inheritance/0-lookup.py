#!/usr/bin/python3
"""Module 0-lookup
find a ist of attributes and methods
"""


def lookup(obj):
    """returns list of available atrributes and methods of an object
        
        args:
            - obj: object to look 
    """
    return dir(obj)

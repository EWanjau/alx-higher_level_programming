#!/usr/bin/python3

def lookup(obj):
    """returns list of available atrributes and methods of an object"""
    att = dir(obj)
    return att

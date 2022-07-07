#!/usr/bin/python3
"""Module 6-load_from_json_file
creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """creates and object from a json file

    Args:
        - filename: json file to convert
    Return: None

    create an object from json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

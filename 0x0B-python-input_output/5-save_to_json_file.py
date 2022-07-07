#!/usr/bin/python3
"""Module 5-save_to_json_file
writes an object to a text file in json format
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a json file

    Args:
        - my_obj: object to write
        - filename: json file to write
    Return: None

    Write an object to a text file
    Use json representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

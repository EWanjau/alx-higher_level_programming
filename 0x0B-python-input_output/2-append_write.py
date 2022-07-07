#!/usr/bin/python3
"""Module 2-append_write
appends to file.
"""


def append_write(filename="", text=""):
    """adds characters to a file

    Args:
        - filename: file to be written
        - text: the message to write
    Return: no of characters added
    """

    with open(filename, mode='a', encoding="UTF-8") as w:
        return w.write(text)

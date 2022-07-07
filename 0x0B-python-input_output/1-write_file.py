#!/usr/bin/python3
"""Module 1-write_file.
writes to file.
"""


def write_file(filename="", text=""):
    """Writes to a file the text specified

    Args:
        - filename: file to be written
        - text: the message to write
    """

    with open(filename, mode='w', encoding="utf-8") as w:
        return w.write(text)

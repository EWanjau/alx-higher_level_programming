#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""


def read_file(filename=""):
    """Reads the file passed as an argument

    Args:
        - filename: file to be opened
    """

    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        print()

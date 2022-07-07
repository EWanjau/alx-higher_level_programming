#!/usr/bin/python3

def read_file(filename=""):
    """Reads the file passed as an argument"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        print()

#!/usr/bin/python3
""" this module has function that prints a text with
two lines after these characters, ., ?, :
"""


def text_indentation(text):
    """prints a text with two lines after special 
    characters
    args:
        text: the text to print
    result: text with lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)]
        )
    print("{}".format(text), end="")
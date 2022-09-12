#!/usr/bin/python3

from logging import exception


def safe_print_integer(value):
    """ prints an integer with "{:d}.format()"
            args:
                value: integer to be printed
            output:
                integer printed
    """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except (TypeError):
        return False

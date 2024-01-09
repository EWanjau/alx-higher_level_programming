#!/usr/bin/python3

def safe_print_integer(value):
    """ prints an integer with "{:d}.format()"
            args:
                value: integer to be printed
            output:
                integer printed
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

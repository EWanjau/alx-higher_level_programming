#!/usr/bin/python3

def safe_print_division(a, b):
    """
    division of two integers

    args:
        a: 1st no
        b: 2nd no

    return: division
    """
    div = 0
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div

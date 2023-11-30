#!/usr/bin/python3

from calculator_1 import *
if __name__ == "__main__":
    """Display function
    arguments:
        a: first int
        b: 2nd int
    Returns:
        the value calculated by functions
        """
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

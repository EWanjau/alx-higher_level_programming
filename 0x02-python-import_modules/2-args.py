#!/usr/bin/python3

import sys
if __name__ == "__main__":
    """Display function
    arguments:
        a: first int
        b: 2nd int
    Returns:
        the value calculated by functions
        """
    count = len(sys.argv) - 1
    if count == 0:
        print("{:s}".format('0 arguments.'))
    elif count == 1:
        print("{:d} {:s}:".format(count, 'argument'))
        print("{:d}: {:s}".format(count, sys.argv[1]))
    else:
        print("{:d} {:s}:".format(count, 'arguments'))
        for i in range(1, count+1):
            print("{:d}: {:s}".format(i, sys.argv[i]))

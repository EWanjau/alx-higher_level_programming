#!/usr/bin/python3

import sys
if __name__ == "__main__":
    """Display function
    arguments:
        command line args
    Returns:
        sum
        """
    count = len(sys.argv)
    result = 0
    for i in range(1, count):
        result += int(sys.argv[i])
    print(result)

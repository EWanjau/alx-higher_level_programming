#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function prints x elements of a list
        args:
            my_list: the input list
            x: the no of elements to print
        output:
            x elements
    """
    try:
        if x is not None:
            for val in range(0, x):
                print("{}".format(my_list[val]), end="")
            print()
            return x
    except (IndexError):
        print()
        return val

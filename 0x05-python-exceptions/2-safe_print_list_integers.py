#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """A function that prints only integers
            args:
                my_list: the list to pick from
                x: the number to loop through
            output:
                list of integers
    """
    try:
        for val in range(0, x):
            if isinstance(my_list[val], int):
                print("{:d}".format(my_list[val]), end="")
        print()
        return x
    except (IndexError):
        print()

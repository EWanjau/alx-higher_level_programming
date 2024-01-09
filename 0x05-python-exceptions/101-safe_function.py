#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """executes a function safely
            args:
                fct: pointer to function result
                args: arguments
            output:
                safe execution of a function
    """
    try:
        return fct(*args)
    except BaseException as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None

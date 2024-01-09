#!/usr/bin/python3

def raise_exception_msg(message=""):
    """raises an exception with a specific message
        args:
            message: the text exception
        output:
            exception raised
    """
    raise NameError("{}".format(message))

#!/usr/bin/python3

def safe_print_division(a, b):
    """ prints results of division
            args:
                a: numerator
                b: denominator
            result:
                quotient
    """
    answer = 0
    try:
        answer = a / b
        return answer
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:0.1f}".format(answer))

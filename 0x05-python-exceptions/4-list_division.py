#!/usr/bin/python3

from unittest import result


def list_division(my_list_1, my_list_2, list_length):
    """divides element by elements in 2 lists
            args:
                my_list_1: list 1
                my_list_2: list 2
                list_length: size of list
            output:
                quotient of both lists
    """
    length = []
    for val in range(0, list_length):
        result = 0
        try:
            result = my_list_1[val] / my_list_2[val]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            length.append(result)
    return length

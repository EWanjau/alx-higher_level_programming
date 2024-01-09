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
    val = 0
    while val < list_length:
        result = 0
        try:
            result = my_list_1[val] / my_list_2[val]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            val += 1
            length.append(result)
    return length

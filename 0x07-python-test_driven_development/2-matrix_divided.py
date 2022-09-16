#!/usr/bin/python3
"""module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """function that divides matrix by div
            args:
                matrix: 1st input
                div: 2nd input
            output:
                a matrix quotient
    """
    if type(matrix) is not list and type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = [[(round(val / div, 2)) for val in row] for row in matrix]
    return new_matrix

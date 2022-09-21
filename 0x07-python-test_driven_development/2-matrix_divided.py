#!/usr/bin/python3
""" this module has function that divides all
elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all the elements in a matrix
    args:
        matrix: the matrix
        div: divisor
    result: divisor
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
            integers/floats")
    for row in range(len(matrix)):
        if type(matrix[row]) is not list or len(matrix[row]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for val in range(len(matrix[row])):
            if type(matrix[row][val]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix

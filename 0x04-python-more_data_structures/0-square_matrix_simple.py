#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[x * x for x in row] for row in matrix]
    return new_matrix

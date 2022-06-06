#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return None
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()

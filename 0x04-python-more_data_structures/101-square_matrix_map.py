#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    computes the square of all integers in amtrix using map

    args:
    matrix  is a 2 dimensional array

    Returns: a new matrix same size as matrix
    each value should be the square of the value of the input
    """

    if matrix is not None:
        return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))

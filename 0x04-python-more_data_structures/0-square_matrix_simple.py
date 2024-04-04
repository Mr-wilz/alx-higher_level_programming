#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of elements in a matrix
    matrix is a 2 D array
    returns a new matrix same size as the first matrix
    """
    return [[element ** 2 for element in row] for row in matrix]

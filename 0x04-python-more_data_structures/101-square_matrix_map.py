#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    if matrix is not None:
        return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers
    """

    for row in matrix:
        for column, element in enumerate(row):
            if column != 0:
                print(" ", end='')
            print("{:d}".format(element), end='')
        print()

#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a given list.
    Return a new list with True or False
    """
    return [num % 2 == 0 for num in my_list]

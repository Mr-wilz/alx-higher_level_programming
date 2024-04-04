#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer).
    You are not allowed to import any module.
    """
    return sum(set(my_list))

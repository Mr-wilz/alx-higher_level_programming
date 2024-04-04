#!/usr/bin/python3
"""a class Mylist that inherits from the built list"""


class MyList(list):
    """Class that inherits from the Base class list

    Args:
     list: list to be sorted
     """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

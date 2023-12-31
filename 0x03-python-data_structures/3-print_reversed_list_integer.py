#!usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints a list in reversed order
    one ineger per line
    """

    if my_list:

        # point i to the last element
        i = len(my_list) - 1

        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1

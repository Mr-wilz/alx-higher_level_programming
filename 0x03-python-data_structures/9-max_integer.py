#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function that finds the biggest integer in a list.
    - my_list: input list of integers
    - Return: max integer or none if list is empty
    """

    if len(my_list) == 0:
        return None
    if len(my_list) > 0:
        max_int = my_list[0]
        for num in  my_list:
            if num > max_int:
                max_int = num
        return max_int

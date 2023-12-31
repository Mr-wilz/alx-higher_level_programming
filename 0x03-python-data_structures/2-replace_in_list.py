#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """function that replaces an element as a specific position
       if idx is less than 0 original list is returned without modification
       if the idx is out of range return original list without modification
    """


    if idx < 0:
        return (my_list)

    length = len(my_list)

    if idx > length - 1:
        return (my_list)

    my_list[idx] = element

    return (my_list)

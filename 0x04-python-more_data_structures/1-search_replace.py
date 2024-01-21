#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    replaces an element of a list by another and prints new list

    Args:
       my_list: is the initial list
       search is the element to replace
       replace is the new element
    """
    new_list = my_list.copy()
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace

    return new_list

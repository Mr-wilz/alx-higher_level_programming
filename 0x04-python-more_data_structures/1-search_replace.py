#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    replaces an element of a list by another and prints new list

    Args:
       my_list: is the initial list
       search is the element to replace
       replace is the new element
    """
    dup = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            dup.append(replace)
        else:
            dup.cappend(my_list[i])
    return dup

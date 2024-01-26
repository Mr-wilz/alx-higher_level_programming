#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: The input dictionary.
        value: The value to search and delete in the dictionary.

    Returns:
        None. The input dictionary is modified in-place.
    """
    keys_list = list(a_dictionary.keys())

    for key in keys_list:
        if value == a_dictionary.get(key):
            del a_dictionary[key]

    return a_dictionary

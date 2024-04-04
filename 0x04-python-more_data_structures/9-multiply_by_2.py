#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary: The input dictionary with integer values.

    Returns:
        A new dictionary with values multiplied by 2.
    """
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary

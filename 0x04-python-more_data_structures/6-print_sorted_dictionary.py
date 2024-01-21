#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.
    You can assume that all keys are strings.
    Keys are sorted by alphabetic order.
    """
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")

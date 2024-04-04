#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The dictionary to be updated.
        key: The key (always a string) to be replaced or added.
        value: The value (any type) to be associated with the key.

    Returns:
        None (The dictionary is modified in place).
    """
    a_dictionary.update([(key, value)])
    return a_dictionary

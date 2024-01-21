#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.
    Key argument will always be a string.
    If a key doesn’t exist, the dictionary won’t change.
    You are not allowed to import any module.
    """
    a_dictionary.pop(key, None)
    return a_dictionary

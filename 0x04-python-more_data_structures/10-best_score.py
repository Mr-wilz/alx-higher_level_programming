#!/usr/bin/python3

def best_score(a_dictionary):
    """
    function that returns a key with the biggest integer value
    if no score is found none is returned
    """
    if a_dictionary is not None and a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None

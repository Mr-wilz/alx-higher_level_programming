#!/usr/bin/python3
"""function that writes an obj to a text file using json rep"""
import json
""" module conatain json funtions"""

def save_to_json_file(my_obj, filename):
    """ Function that writes an object to a text file
    by a JSON representation

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""returns an obj rep by a a JSON string"""
import json
""" module containing the function to json atring"""


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): JSON string.

    Returns:
        obj: Python data structure represented by the JSON string.
    """
    return json.loads(my_str)

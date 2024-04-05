#!/usr/bin/python3
""" appends a string (text) at the end of a text file
returns the number of characters added"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
        num_characters = len(text)
    return num_character

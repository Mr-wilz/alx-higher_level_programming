#!/usr/bin/python3

def no_c(my_string):
    """function that removes all c characters from a string    
    """
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string

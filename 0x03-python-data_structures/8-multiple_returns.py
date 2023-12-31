#!/usr/bin/python
def multiple_returns(sentence):
    """Function that returns a tuple with the length of a string
    and the first character
    """

    if len(sentence) == 0:
        return (0, None)
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
        return (length, first_char)

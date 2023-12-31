#!/usr/bin/python
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    if sentence:
        length = len(sentence)
        first_char = sentence[0]
        return (length, first_char)

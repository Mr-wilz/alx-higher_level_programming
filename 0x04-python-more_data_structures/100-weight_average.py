#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple

    Args:
        my_list: A list of tuples, each containing a score and weight.

    Returns:
        The weighted average as a float. Returns 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_score / total_weight

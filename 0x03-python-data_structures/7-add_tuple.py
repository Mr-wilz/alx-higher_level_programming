#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.

    Args:
    - tuple_a (tuple): The first tuple.
    - tuple_b (tuple): The second tuple.

    Returns:
    - tuple: A tuple with the addition of corresponding elements
    """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result_tuple

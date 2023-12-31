#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
    - my_list (list): The input list.
    - idx (int): The index of the item to be deleted.

    Returns:
    - list: The modified list after deleting the item.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:idx] + my_list[idx + 1 :]

    return new_list

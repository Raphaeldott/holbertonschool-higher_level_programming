#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number.

    Args:
        my_list (list): The list of integers.
        number (int): The multiplier.

    Returns:
        list: A new list with values multiplied by number.
    """
    return list(map(lambda x: x * number, my_list))

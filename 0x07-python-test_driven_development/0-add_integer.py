#!/usr/bin/python3
"""
This module contains function
that returns the sum of 2 integers a and b.
"""


def add_integer(a, b=98) -> int:
    """
    Computes and returns the sum of 
    2 integers a and b.

    Args:
        a (int | float): First number to be added.
        b (int | float): Second number to be added.

    Raises:
        TypeError: If either of the inputs is not an integer or float.

    Returns:
        int: Sum of the a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

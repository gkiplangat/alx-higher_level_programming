#!/usr/bin/python3
"""
Returns true if it is an instance of object
"""


def inherits_from(obj, a_class):
    """
    Checks if `obj` is an instance of `a_class` or `object`.
    Args:
        obj (any): Any data type
        a_class (ant): Any class object

    Returns:
        bool: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

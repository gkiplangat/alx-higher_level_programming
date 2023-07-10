#!/usr/bin/python3
"""
Defines a class MyList.
"""


class MyList(list):
    """
    This is a Custom class that inherits from `list`.
    """
    def print_sorted(self):
        """
        Prints the list item in sorted order.
        """
        print(sorted(self))

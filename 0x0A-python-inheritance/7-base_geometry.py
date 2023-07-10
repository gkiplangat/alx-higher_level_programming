#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry():
    """
    BaseGeometry empty class
    """

    def area(self):
        """
        Not implemented therefore raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method that validates the input value

        Args:
            name (str): value that's always a string
            value (int): value greater than 0

        Returns:
        TypeError: if value is not an int
        ValueError: if value is not a positive integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

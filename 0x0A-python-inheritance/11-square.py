#!/usr/bin/python3

"""
Square #1 Class Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Define the Square class
    """

    def __init__(self, size):
        """
        Initialize square method
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Compute & return area of square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Method that returns a string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

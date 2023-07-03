#!/usr/bin/python3
"""
This module defines the widht and height of a rectangle
"""


class Rectangle:
    """This is the Representation of the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializing a rectangle instance.

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            Getter function for private variable, width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            Setter function for private variable, width.

            Args:
                value (int): The new width to set.
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """
            Getter function for private variable, height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """
            Setter function for private variable, height.

            Args:
                value (int): The new height to set.
            """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

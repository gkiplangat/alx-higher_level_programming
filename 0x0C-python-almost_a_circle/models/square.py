#!/usr/bin/python3
"""
Creating a square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defining square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing square class

         Args:
            size (int): The length of one side of the square.
            x (int, optional): The x-coordinate of the top-left
                               corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left
                               corner of the square. Defaults to 0.
            id (str, optional): A unique identifier for the square.
                               Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Printing square class by overloading __str__ method
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """
        Getting size of square
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Setting size of square
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updating square class

        Args:
            *args (tuple): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returning dictionary representation of square
        """

        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }

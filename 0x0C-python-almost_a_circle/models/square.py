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
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Printing square class by overloading __str__ method
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Size<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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

    def update(self,*newA, **newAv):
        """
        Update square class

        Args:
            *newA (tuple): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
            **newAv (dict): New key/value pairs of attributes.
        """

        if newA not None and len(newA) != 0:
            if len(newA) >= 1:
                if type(newA[0]) != int and newA[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = newA[0]
            if len(newA) > 1:
                self.size = newA[1]
            if len(newA) > 2:
                self.x = newA[2]
            if len(newA) > 3:
                self.y = newA[3]
        else:
            for key, value in newAv.items():
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
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

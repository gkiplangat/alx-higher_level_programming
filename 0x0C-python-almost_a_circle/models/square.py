#!/usr/bin/python3
"""Creating a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    # Overriding the width and height setters
    # to keep them equal (since Square has only one side)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._height = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._width = value
        self._height = value

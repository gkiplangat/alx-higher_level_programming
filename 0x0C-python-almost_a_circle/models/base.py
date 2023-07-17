#!/usr/bin/python3
"""
    Base Module
"""

import csv
import json
import turtle
from pathlib import Path


class Base:
    """
    Base class which will be inherited by all other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

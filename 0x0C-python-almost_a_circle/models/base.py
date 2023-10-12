#!/usr/bin/python3
"""Base class"""


class Base:
    """Base class for all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the instance with an id."""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

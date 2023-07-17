#!/usr/bin/python3
"""
models/square.py
square class model
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initaializing square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ instance string representation """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Update the class Square
        that assigns an argument to each attribute
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribut
        """
        if len(args) != 0:
            i = 0
            for arg in args:
                i += 1
                if (i == 1):
                    self.id = arg
                elif (i == 2):
                    self.size = arg
                elif (i == 3):
                    self.x = arg
                elif (i == 4):
                    self.y = arg
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return ({"id" : self.id, "size" : self.size,
                 "x" : self.x, "y" : self.y})

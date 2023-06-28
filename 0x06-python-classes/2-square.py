#!/usr/bin/python3
""" Defining a square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """ init a square instance """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

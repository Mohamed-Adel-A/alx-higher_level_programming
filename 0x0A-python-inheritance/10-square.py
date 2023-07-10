#!/usr/bin/python3
""" 8. Rectangle """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square (Rectangle):
    """ subcalss from Rectangle """
    def __init__(self, size):
        """
        init Rectangle instance
        """
        self.integer_validator("width", size)
        self.__size = size

    def area(self):
        """ return the area """
        return (self.__size * self.__size)

    def __str__(self):
        """ ___str___ implementation """
        s = "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
        return (s)

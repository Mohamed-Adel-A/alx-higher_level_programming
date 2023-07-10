#!/usr/bin/python3
""" 8. Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ subcalss from Rectangle """
    def __init__(self, size):
        """
        init Rectangle instance
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

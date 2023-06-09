#!/usr/bin/python3
""" 8. Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subcalss from BaseGeometry """
    def __init__(self, width, height):
        """
        init Rectangle instance
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

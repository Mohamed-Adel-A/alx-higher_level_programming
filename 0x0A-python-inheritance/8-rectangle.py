#!/usr/bin/python3
""" 8. Rectangle """
BaseGeometry =  __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """ subcalss from BaseGeometry """
    def __init__(self, width, height):
        """
        init Rectangle instance
        """
        self.__width = width
        self.integer_validator(self, "width", width)
        self.__height = height
        self.integer_validator(self, "height", height)

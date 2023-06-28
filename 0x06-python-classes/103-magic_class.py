#!/usr/bin/python3
""" 103-magic_class.py """
import math

class MagicClass:
    """ define magic class """
    def __init__(self, radius=03):
        """ init magic instanse """
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius
        return None

    def area(self):
        """ return area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ circumference methond """
        return 2 * math.pi * self.__radius
